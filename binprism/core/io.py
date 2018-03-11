from .FourierSeries import FourierSeries
from .PPD import PPD
from .Profile import Profile
from struct import pack, unpack
import numpy as np
import codecs

class save:
    '''
    Class for writing profiles. Must be iterable of profiles.

    Parameters
    ----------
    profiles (iterable):
        Iterable of binprism.Profile objects
    '''
    def __init__(self, profiles):
        self.profiles = profiles

    def txt(self, fp):
        '''
        Saves profiles to an encoded text file

        Parameters
        ----------
        fp (str):
            Filepath to save to
        '''
        lines = []
        for profile in self.profiles:
            line = ''

            packed_total = pack('f', profile.total)
            for byte in packed_total:
                line += chr(byte)

            packed_start = pack('f', profile.time_range[0])
            for byte in packed_start:
                line += chr(byte)

            packed_end = pack('f', profile.time_range[1])
            for byte in packed_end:
                line += chr(byte)

            packed_average = pack('f', np.real(profile.dist.L.c[0]))
            for byte in packed_average:
                line += chr(byte)

            for coeff in profile.dist.L.c[1:]:
                packed_real = pack('f', np.real(coeff))
                for byte in packed_real:
                    line += chr(byte)
                packed_imag = pack('f', np.imag(coeff))
                for byte in packed_imag:
                    line += chr(byte)

            lines.append(line)

        f = codecs.open(fp, 'w', 'utf-8')
        f.write(chr(9587).join(lines))
        f.close()

    def df(self):
        '''
        Places information on profiles into a Pandas data frame. Columns are:
            `Total`: Total number of events
            `Start`: Start time of the time_range
            `End`: End time of the time_range
            `c0`: DC component of the log-pdf's Fourier series
            `Re(ck)`: The real part of element k of the log-pdf's Fourier series
            `Im(ck)`: The imaginary part of element k of the log-pdf's Fourier series

        Returns
        -------
        df (pandas.DataFrame):
            Data frame with information on each profile
        '''
        import pandas as pd
        K = 0
        for profile in self.profiles:
            K = max(K, profile.dist.log_pdf_coef.n_harmonics)

        cols = ['Total', 'Start', 'End', 'c0']
        for k in range(1, K+1):
            cols.append('Re(c%d)'%(k))
            cols.append('Im(c%d)'%(k))

        N = len(self.profiles)
        df = pd.DataFrame(np.empty((N, 2*K+4)), columns = cols)
        for i in range(N):
            row = [self.profiles[i].total, self.profiles[i].time_range[0], self.profiles[i].time_range[1], np.real(self.profiles[i].dist.log_pdf_coef[0])]
            for k in range(1, K+1):
                coef = self.profiles[i].dist.log_pdf_coef[k]
                row += [np.real(coef), np.imag(coef)]
            df.loc[i] = row

        return df

    def csv(self, fp):
        '''
        Saves profile list as a csv by first creating a data frame and then saving that data frame as a csv

        Parameters
        ----------
        fp (str):
            Filepath to save profiles to
        '''
        try:
            import pandas as pd
            df = save(self.profiles).df()
            df.to_csv(fp, index = False)
        except ImportError:
            #Make this an external tool
            K = 0
            for profile in self.profiles:
                K = max(K, profile.dist.log_pdf_coef.n_harmonics)

            cols = ['Total', 'Start', 'End', 'c0']
            for k in range(1, K+1):
                cols.append('Re(c%d)'%(k))
                cols.append('Im(c%d)'%(k))

            N = len(self.profiles)
            rows = []
            for i in range(N):
                row = [self.profiles[i].total, self.profiles[i].time_range[0], self.profiles[i].time_range[1], np.real(self.profiles[i].dist.log_pdf_coef[0])]
                for k in range(1, K+1):
                    coef = self.profiles[i].dist.log_pdf_coef[k]
                row += [np.real(coef), np.imag(coef)]
                for j in range(len(row)):
                    row[j] = str(row[j])
                rows.append(row)

            lines = [','.join(cols)]
            for row in rows:
                lines.append(','.join(row))

            f = open(fp, 'w')
            f.write('\n'.join(lines))
            f.close()

class load:
    '''
    Class for loading profiles
    '''
    def __init__(self, profiles):
        self.profiles = profiles

    def __getitem__(self, key):
        return self.profiles[key]

    @classmethod
    def txt(cls, fp):
        
        f = codecs.open(fp, 'r', 'utf-8')
        lines = f.read().split(chr(9587))
        f.close()

        profiles = []
        for line in lines:
            total_encoded = line[:4]
            byte_list = []
            for character in total_encoded:
                byte_list.append(ord(character))
            total = unpack('f', bytes(byte_list))[0]
            
            start_encoded = line[4:8]
            byte_list = []
            for character in start_encoded:
                byte_list.append(ord(character))
            start = unpack('f', bytes(byte_list))[0]

            end_encoded = line[8:12]
            byte_list = []
            for character in end_encoded:
                byte_list.append(ord(character))
            end = unpack('f', bytes(byte_list))[0]

            average_encoded = line[12:16]
            byte_list = []
            for character in average_encoded:
                byte_list.append(ord(character))
            average = unpack('f', bytes(byte_list))[0]

            coeff = [average]
            for i in range(16, len(line), 8):
                real_encoded = line[i:i+4]
                byte_list = []
                for character in real_encoded:
                    byte_list.append(ord(character))
                real = unpack('f', bytes(byte_list))[0]
                imag_encoded = line[i+4:i+8]
                byte_list = []
                for character in imag_encoded:
                    byte_list.append(ord(character))
                imag = unpack('f', bytes(byte_list))[0]
                coeff.append(real + 1j*imag)

            profile = Profile(PPD(FourierSeries(coeff)), total, (start, end))
            profiles.append(profile)

        return cls(profiles)

    @classmethod
    def df(cls, df):
        '''
        Read in profiles from Pandas data frame

        Parameters
        ----------
        df (pandas.DataFrame):
            Pandas data frame containing information on profiles. Must have the following columns:
                `Total`: Total number of events
                `Start`: Start time of the time_range
                `End`: End time of the time_range
                `c0`: DC component of the log-pdf's Fourier series
                `Re(ck)`: The real part of element k of the log-pdf's Fourier series
                `Im(ck)`: The imaginary part of element k of the log-pdf's Fourier series
        '''
        K = (len(df.columns)-4) // 2
        profiles = []
        for ix in df.index:
            total = df.loc[ix, 'Total']
            time_range = tuple(df.loc[ix, ['Start', 'End']])
            c = [df.loc[ix, 'c0']]
            for k in range(1, K+1):
                c.append(df.loc[ix, 'Re(c%d)'%(k)] + 1j*df.loc[ix, 'Im(c%d)'%(k)])

            profiles.append(Profile(PPD(FourierSeries(c)), total, time_range))

        return cls(profiles)

    @classmethod
    def csv(cls, fp):
        '''
        Read in profiles from csv with information on them

        Parameters
        ----------
        fp (str): Filepath to read from. Must be a table containing the columns specified in load.df()
        '''
        import pandas as pd
        df = pd.read_csv(fp)
        return load.df(df)