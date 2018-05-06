# binprism.fit
**`binprism.fit(data, bins, n_harmonics, time_range)`** <br />
Fits a profile to best match binned data by solving the linear system of equations described in the [methodology](methodology.md) section.

## Parameters
**data (array-like):** *Data to fit profile to match* <br />
**bins (array-like):** *Start time of each data bin. The length must be the same as* `data` <br />
**n_harmonics (int):** *Maximum number of harmonics used in fitting the log-pdf of the underlying distribution* <br />
**time_range (tuple):** *Length-2 tuple indicating the values that map to 0 and 2&pi;, respectively, in the underlying distribution*

## Returns
**Profile (binprism.Profile):** *Profile fit from input data*

## Example
```
>>> data = np.array([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200])
>>> bins = range(0, 24, 2)
>>> profile = bp.fit(data, bins, 5, (0, 24))
>>> plt.bar(bins, data/2, 2, align = 'edge', facecolor = '#c0c0c0', edgecolor = 'k')
>>> profile.plot(288, color = 'b', linewidth = 3)
>>> plt.xlim(profile.time_range)
>>> plt.xticks(range(0, 25, 4))
>>> plt.xlabel('Hour of Day')
>>> plt.ylabel('Events per Hour')
>>> plt.grid(True)
>>> plt.show()
```
![alt text](Profile/ProfilePlotExample.png "Profile.plot() Example")
