from __future__ import division
from .FourierSeries import FourierSeries
from .PPD import PPD
from .tools import counting
import numpy as np
from scipy.special import i0
from math import pi, log
from datetime import time, datetime
from dateutil.tz import tzlocal
import matplotlib.pyplot as plt

class Profile:
    '''
    Demand profile

    Parameters
    ----------
    dist (spectranspo.PPD):
        Probability distribution that events follow
    total (numeric):
        Total number of events
    time_range (tuple):
        Length-2 tuple indicating the values of time that map to 0 and 2π, respectively, in the underlying distribution
    '''
    def __init__(self, dist, total, time_range = (0, 24)):
        
        self.dist = dist
        self.total = float(total)
        self.time_range = time_range
        self.mean_time = self.angle2time(dist.mean())

    def __str__(self):
        return 'spectranspo.Profile\nTotal Events: {0}\nTime Range:  {1}\nMean Time: {2}\nPDF: {3}'.format(self.total,
                                                                                                           self.time_range,
                                                                                                           self.time2hhmm(self.mean_time),
                                                                                                           self.dist)

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        self_hourly = self['hourly']
        other_hourly = other['hourly']
        return Profile.from_counts(self_hourly + other_hourly, np.arange(24), self.dist.L.K, self.time_range)

    def __mul__(self, other):
        return Profile(self.dist, other*self.total, self.time_range)

    def __neg__(self):
        return Profile(self.dist, -self.total, self.time_range)

    def __sub__(self, other):
        return self + (-other)

    def __truediv__(self, other):
        return self * (1/other)

    def __getitem__(self, *args):

        if args[0] == 'hourly':
            return counting.array(self, np.linspace(self.time_range[0], self.time_range[1], 24, False))
        
        elif args[0] == '15min':
            return counting.array(self, np.linspace(self.time_range[0], self.time_range[1], 96, False))

        elif type(args[0]) == 'str':
            raise ValueError('Invalid TimeDist index. Must be iterable, numeric, slice, "hourly", or "15min".')

        if type(args[0]) == slice:
            if args[0].step == None:
                return self.count_events(args[0].start, args[0].stop)
            else:
                return counting.array(self, np.arange(args[0].start, args[0].stop + args[0].step, args[0].step))[:-1]

        if type(args[0]) == int or type(args[0]) == float:
            return self.count_events(0, args[0])

        return counting.array(self, args[0])

    def time2angle(self, t):
        '''
        Converts a time in the profile's units to angle that the earth has rotated since the day began in radians

        Parameters
        ----------
        t (float or array-like)
            Time(s) to convert to angles

        Returns
        -------
        theta (float or array-like)
            Angle(s) that have been converted
        '''
        return 2*pi*((t - self.time_range[0])/(self.time_range[1] - self.time_range[0]))

    def angle2time(self, theta):
        '''
        Converts angle that the Earth has rotated since the beginning of the day in radians to units specified by time_range

        Parameters
        ----------
        theta (float or array-like):
            Angle(s) to convert to time

        Returns
        -------
        t (float or array-like):
            Time(s) that have been converted
        '''
        return self.time_range[0] + (self.time_range[1] - self.time_range[0])/(2*pi)*theta

    def time2hhmm(self, t, format24 = None):
        '''
        Converts a time value to a time in hh:mm format.

        Parameters
        ----------
        t (numeric):
            Time to display
        format24 (bool):
            Indicates whether or not to use 24-hour time format. If not specified, inferred based on local time zone.
        '''
        if format24 is None:
            if datetime.now(tzlocal()).tzname()[:2] == 'US':
                format24 = False
            else:
                format24 = True
        theta = self.time2angle(t)
        hours = 24/(2*pi)*theta
        hr = int(hours // 1)
        mn = int(60*(hours % 1))
        tod = time(hr, mn)
        if format24:
            return tod.strftime('%H:%M')
        else:
            outtime = tod.strftime('%I:%M %p')
            if outtime[0] == '0':
                return outtime[1:]
            else:
                return outtime
        
    @classmethod
    def from_counts(cls, counts, breaks, K, time_range = (0, 24)):
        '''
        Fit profile from binned counts

        Parameters
        ----------
        counts (array-like):
            Array of counts
        breaks (array-like):
            Start times of each count period. The length must be the same as breaks
        K (int):
            Maximum number of Fourier coefficients to use in the underlying distribution
        time_range (tuple):
            Length-2 tuple indicating the values of time that map to 0 and 2π, respectively, in the underlying distribution
        '''
        for b in breaks:
            if b < time_range[0] or b >= time_range[1]:
                raise ValueError('Bin breaks must be within time_range')

        assert len(breaks) == len(counts), 'Counts and breaks must have same length.'

        N = len(counts)
        counts = np.array(counts)
        breaks = 2*pi*(np.array(breaks) - time_range[0])/(time_range[1] - time_range[0])
        breaks = np.append(breaks, 2*pi)
        widths = np.diff(breaks)
        total = counts.sum()
        props = counts / total

        #Create matrix for OLS
        X = np.zeros((N, 2*K+1), np.complex)
        for i in range(N):
            a = breaks[i]
            b = breaks[i+1]
            X[i, 0] = b - a
            for k in range(1, K+1):
                X[i, k] = -1j/k*(np.exp(1j*k*b) - np.exp(1j*k*a))
                X[i, -k] = np.conj(X[i, k])

        #Comute best coefficients via ordinary least squares regression
        y = widths*np.log(props/widths)
        XTX = np.dot(X.T, X)
        XTy = np.dot(X.T, y)
        c = np.linalg.solve(XTX, XTy)[:K+1]

        #Create distribution
        fs = FourierSeries(c)
        dist = PPD(fs)
        return cls(dist, total, time_range)

    def shift(self, amount):
        '''
        Shifts the profile by the specified amount

        Parameters
        ----------
        amount (numeric):
            Amount in the units specified by time_dist to shift the demand
        '''
        phi = self.time2angle(amount)
        return Profile(PPD(self.dist.L.shift(phi, False)), self.total, self.time_range)

    def eval(self, t):
        '''
        Evaluates the event rate at time t
        
        parameters
        ----------
        t (numeric or array-like):
            Time(s) at which to evaluate the event rate in the units specified by time_range

        Returns
        -------
        flow (numeric or array-like):
            Event rate evaluated at time t
        '''
        return 2*pi/(self.time_range[1] - self.time_range[0])*self.total*self.dist.pdf(self.time2angle(t))

    def count_events(self, a, b):
        '''
        Counts the number of events between times a and b

        Parameters
        ----------
        a (numeric or array-like):
            Time(s) at which to start counting events
        b (numeric or array-like):
            Time(s) at which to end counting events

        Returns
        -------
        n_events (numeric or array-like):
            Number of events between a and b
        '''
        theta_a = 2*pi * (a / (self.time_range[1] - self.time_range[0]) + self.time_range[0])
        theta_b = 2*pi * (b / (self.time_range[1] - self.time_range[0]) + self.time_range[0])
        return self.total*(self.dist.cdf(theta_b) - self.dist.cdf(theta_a))
   
    def sim(self, N, **kwargs):
        '''
        Simulates N random events following the profile's underlying distribution but converted to the profile's time units

        Parameters
        ----------
        N (int):
            Number of events to simulate
        kwargs:
            spectranspo.PPD.sim keyword arguments

        Returns
        -------
        events (length-N array):
            Simulated events
        '''
        return self.angle2time(self.dist.sim(N, **kwargs))

    def plot(self, N, circular = False, **kwargs):
        '''
        Plots the profile.

        Parameters
        ----------
        N (int):
            Plotting resolution
        circular (bool):
            If True, the profile will be plotted on a circular domain. If False, it will be plotted on a linear domain
        kwargs:
            matplotlib.pyplot.plot() keyword arguments
        '''
        t = np.linspace(self.time_range[0], self.time_range[1], N+1)
        v = self.eval(t)
        if circular:
            z = np.exp(1j*self.time2angle(t))
            plt.plot(v*np.imag(z), v*np.real(z), **kwargs)
        else:
            plt.plot(t, v, **kwargs)