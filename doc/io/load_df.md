# binprism.load.df
**`binprism.load.df(fp)`** <br />
Read in profiles from Pandas data frame. Must have the following columns:
**Total:** Total number of events <br />
**Start:** Start time of the time_range <br />
**End:** End time of the time_range <br />
**c0:** DC component of the log-pdf's Fourier series <br />
**Re(ck):** The real part of element k of the log-pdf's Fourier series <br />
**Im(ck):** The imaginary part of element k of the log-pdf's Fourier series <br />

# Parameters
**df (pandas.DataFrame):** *Pandas data frame containing information on profiles. Must have the necessary columns:*

# Example
>>> cols = ['Total', 'Start', 'End', 'c0',
...         'Re(c1)', 'Im(c1)', 'Re(c2)', 'Im(c2)', 'Re(c3)', 'Im(c3)',
...         'Re(c4)', 'Im(c4)', 'Re(c5)', 'Im(c5)', 'Re(c6)', 'Im(c6)']
>>> row1 = [43398, 0, 24, -2.072574359,
...         -0.327883405, 0.340836381, -0.068659837, 0.258643049, 0.135607283, 0.080998411,
...         0.0141557, 0.001157863, -0.026685376, 0.004407908, 0.010182986, 0.011588839]
>>> row2 = [41277, 0, 24, -2.07003999,
...         -0.387332858, 0.21029823, -0.140071343, 0.288783925, 0.085234011, 0.1425885,
...         0.061657289, -0.01820986, -0.019192808, -0.031632466, -0.027056588, -0.001741802]
>>> df = pd.DataFrame(columns = cols)
>>> df.loc[0] = row1
>>> df.loc[1] = row2
>>> profiles = bp.load.df(df)
>>> profiles[0].plot(288, color = 'r', label = 'Profile 1')
>>> profiles[1].plot(288, color = 'b', label = 'Profile 2')
>>> plt.xlim(profiles[0].time_range)
>>> plt.legend(loc = 'best')
>>> plt.show()
[alt text](FromDFExample.png "Example of reading profiles from data frame")
