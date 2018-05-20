# binprism.save.df
**`binprism.save.df()`** <br />
Places information on profiles into a Pandas data frame. Columns are: <br />
**Total:** Total number of events <br />
**Start:** Start time of the `time_range` <br />
**End:** End time of the `time_range` <br />
**c0:** DC component of the log-pdf's Fourier series <br />
**Re(ck):** The real part of element k of the log-pdf's Fourier series <br />
**Im(ck):** The imaginary part of element k of the log-pdf's Fourier series <br />

## Returns
**df (pandas.DataFrame):** *Data frame with information on each profile*

## Example
```
>>> eb_counts = [590, 353, 301, 230, 393, 655, 1469, 2067, 2549, 2375, 1783, 2076, 
...              2193, 2017, 2513, 3262, 3294, 2915, 2657, 2412, 2323, 1928, 1925, 1118]
>>> wb_counts = [387, 316, 237, 219, 442, 1491, 2472, 2716, 2809, 2294, 2159, 1991,
...              2380, 2119, 2052, 2333, 2434, 2122, 2188, 2385, 1821, 1760, 1314, 836]
>>> hours = range(24)
>>> n_harmonics = 6
>>> time_range = (0, 24)
>>> eb_profile = bp.fit(eb_counts, hours, n_harmonics, time_range)
>>> wb_profile = bp.fit(wb_counts, hours, n_harmonics, time_range)
>>> df = bp.save([eb_profile, wb_profile]).df()
>>> df
     Total  Start   End        c0    Re(c1)    Im(c1)    Re(c2)    Im(c2)  \
0  43398.0    0.0  24.0 -2.072574 -0.327883  0.340836 -0.068660  0.258643   
1  41277.0    0.0  24.0 -2.070040 -0.387333  0.210298 -0.140071  0.288784   

     Re(c3)    Im(c3)    Re(c4)    Im(c4)    Re(c5)    Im(c5)    Re(c6)  \
0  0.135607  0.080998  0.014156  0.001158 -0.026685  0.004408  0.010183   
1  0.085234  0.142588  0.061657 -0.018210 -0.019193 -0.031632 -0.027057   

     Im(c6)  
0  0.011589  
1 -0.001742 
```
