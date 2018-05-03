# binprism.PPD.mean
**`PPD.mean()`** <br />
Returns the mean angle of the distribution

## Returns
**mean (float):** *Mean angle of the distribution in radians*

## Example
```
>>> fs = bp.FourierSeries([-2, 0.6 + 0.75j, -0.4 + 0.3j])
>>> dist = bp.PPD(fs)
>>> dist.mean()
5.1972328284356459
>>> x = np.linspace(0, 2*np.pi, 250)
>>> plt.plot(x, dist.pdf(x), color = 'b')
>>> plt.plot(2*[dist.mean()], [0, dist.pdf(dist.mean())], color = 'k', linestyle = ':')
>>> plt.text(dist.mean(), 1.1*dist.pdf(dist.mean()), "$\mu={}$".format(round(dist.mean(), 3)),
             ha = "center", va = "center")
>>> plt.grid(True)
>>> plt.xlim(0, 2*np.pi)
>>> plt.ylim(0, 1)
>>> plt.show()
```
![alt text](MeanExample.png "PPD.mean() example")
