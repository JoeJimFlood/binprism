# binprism.FourierSeries.log
**`FourierSeries.log(tol = 2**-23, max_iter = 1000)`** <br />
Finds the Fourier coefficients of the natural logarithm of the wave using a Taylor series. If any part of the wave is negative, an error will be raised.
## Parameters
**tol (float):** *Tolerance for Taylor series approximation* <br />
**max_iter (int):** *Maximum number of Taylor series iterations*
## Returns
**out (binprism.FourierSeries):** *Natural logarithm of Fourier series*
## Example
```
>>> fs = bp.FourierSeries([10, 2j, -0.5j])
>>> x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
>>> np.log(fs.eval(x))
array([ 2.30258509,  1.79175947,  2.30258509,  2.63905733,  2.30258509])
>>> fs.log().eval(x)
### FIX ISSUES ###
```