# binprism.FourierSeries.antiderivative
**`FourierSeries.antiderivative()`** <br />
Returns Fourier series of the nonlinear components of the antiderivative of the Fourier series
## Returns
**antiderivative (binprism.FourierSeries):** *Fourier series of the nonlinear parts of the antiderivative*

## Example
```
>>> import binprism as bp
>>> fs = bp.FourierSeries([2, 1 - 0.5j, -0.2 + 0.6j])
>>> fs
2.0 + (2.0)cos(x) + (1.0)sin(x) + (-0.4)cos(2x) + (-1.2)sin(2x)
>>> antiderivative = fs.antiderivative()
>>> antiderivative
0.0 + (-1.0)cos(x) + (2.0)sin(x) + (0.6)cos(2x) + (-0.2)sin(2x)
```
