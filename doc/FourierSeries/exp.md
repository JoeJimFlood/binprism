# binprism.FourierSeries.exp
**`FourierSeries.exp(tol = 2**-23, max_iter = 1000)`** <br />
Finds the Fourier coefficients of the exponentiated wave using a Taylor series
## Parameters
**tol (float):** *Tolerance for Taylor series approximation* <br />
**max_iter (int):** *Maximum number of Taylor series iterations*
## Returns
**out (binprism.FourierSeries):** *Exponentiated Fourier series*
## Example
```
>>> fs = bp.FourierSeries([-4, 2 + 2j, -0.1 - 1j])
>>> x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
>>> np.exp(fs.eval(x))
array([  8.18730753e-01,   4.09734979e-04,   2.74653570e-04,

         1.22140276e+00,   8.18730753e-01])
>>> fs.exp().eval(x)
array([  8.18730753e-01,   4.09734979e-04,   2.74653570e-04,

         1.22140276e+00,   8.18730753e-01])
```