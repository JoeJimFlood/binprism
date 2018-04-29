# binprism.FourierSeries.eval
**`FourierSeries.eval(x)`** <br />
Evaluates the Fourier series at the value(s) x
## Parameters
**x (numeric or array-like):** *X-value(s) of point(s) to evaluate the Fourier series*
## Returns
**y (numeric or array-like):** *Y-value(s) of Fourier series evaluated at x*
## Example
```
>>> x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
>>> fs1 = bp.FourierSeries([0, 0.5]) #Cosine function
>>> fs1.eval(x)
array([  1.00000000e+00,   6.12323400e-17,  -1.00000000e+00,
        -1.83697020e-16,   1.00000000e+00])
>>> fs2 = bp.FourierSeries([3, 0.5 + 0.1j, -0.05 - 0.2j])
>>> fs2.eval(x)
array([ 3.9,  2.9,  1.9,  3.3,  3.9])
```
