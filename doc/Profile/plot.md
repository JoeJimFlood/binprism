# binprism.Profile.plot
**`Profile.plot(N, circular = False, **kwargs)`**
Plots the profile

## Parameters
**N (int):** *Plotting resolution* <br />
**circular (bool):** *If True, the profile will be plotted on a circular domain. If False, it will be plotted on a linear domain* <br />
**kwargs:** *[matplotlib.pyplot.plot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html) keyword arguments*

## Example
```
>>> data = np.array([100, 200, 250, 300, 250, 100, 50, 50, 100, 150, 250, 200])
>>> bins = range(0, 24, 2)
>>> profile = bp.fit(data, bins, 5, (0, 24))
>>> plt.bar(bins, data/2, 2, align = 'edge', facecolor = '#c0c0c0', edgecolor = 'k')
>>> profile.plot(288, color = 'b', linewidth = 3)
>>> plt.xlim(0, 24)
>>> plt.xticks(range(0, 25, 4))
>>> plt.xlabel('Hour of Day')
>>> plt.ylabel('Events per Hour')
>>> plt.grid(True)
>>> plt.show()
```
![alt text](ProfilePlotExample.png "Profile.plot() Example")
