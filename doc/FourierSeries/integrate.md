# binprism.FourierSeries.integrate
**`FourierSeries.integrate(a, b)`** <br />
Integrates the function represented by the Fourier series from `a` to `b`.
## Parameters
**a (numeric or array-like):** *Start of integration* <br />
**b (numeric or array-like):** *End of integration*
## Returns
**result (numeric or array-like):** *Integration result*
## Examples
```
>>> fs = bp.FourierSeries([0, -0.5j]) #f(x) = sin(x)
>>> fs.integrate(0, np.pi)
array(2.0)
>>> fs.integrate([0, 0, 0, 0, 0], [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
### FIX THIS ###
```