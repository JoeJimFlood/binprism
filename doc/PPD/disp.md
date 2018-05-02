# binprism.PPD.disp
**`PPD.disp()`** <br />
Returns the circular dispersion of the distribution

## Returns
**disp (float):** *Circular dispersion of the distribution*

## Example
```
>>> fs = bp.FourierSeries([-2, -0.7j, 0.5 - 0.1j])
>>> dist = bp.PPD(fs)
>>> dist.disp()
2.591293872227488
```
