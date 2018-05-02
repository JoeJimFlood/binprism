# binprism.PPD.cdf
**`PPD.cdf(theta)`** <br />
Cummulative distribution function at `theta`

## Parameters
**theta (numeric or array-like):** *Angle at which to evaluate the CDF*

## Returns
**F (numeric or array-like):** *CDF evaluated at* `theta`

## Example
```
>>> fs = bp.FourierSeries([-2, 0.5 + 0.1j, 0.25 - 0.2j])
>>> dist = bp.PPD(fs)
>>> x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.])
>>> dist.cdf(x)
array([ 0.        ,  0.46233013,  0.52598644,  0.6593879 ,  1.00000007])
```
