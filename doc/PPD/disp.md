# binprism.PPD.disp
**`PPD.disp()`**
Returns the circular dispersion of the distribution

## Returns
**disp (float):** *Circular dispersion of the distribution*

## Example
```
>>> fs = bp.FourierSeries([-2, -0.7j, 0.05 - 0.01j])
>>> dist = bp.PPD(fs)
>>> dist.disp()
1.4243545417343204
```
