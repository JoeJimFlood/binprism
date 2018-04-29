# binprism.FourierSeries.copy
**`FourierSeries.copy()`** <br />
Creates a copy of the Fourier series object.
## Returns
**copy (binprism.FourierSeries):** *Copy of input Fourier Series*

## Example
```
>>> fs1 = bp.FourierSeries([3, 2 + 1j])
>>> fs1
3.0 + (4.0)cos(x) + (-2.0)sin(x)
>>> fs2 = fs1.copy()
>>> fs2
3.0 + (4.0)cos(x) + (-2.0)sin(x)
```
