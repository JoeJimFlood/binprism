# binprism.PPD.var
**`PPD.var()`** <br />
Returns the circular variance of the distribution

## Returns
**var (float):** *Circular variance of the distribution*

## Example
```
>>> fs = bp.FourierSeries([-2, -0.7j, 0.05 - 0.01j])
>>> dist = bp.PPD(fs)
>>> dist.disp()
1.4243545417343204
```
