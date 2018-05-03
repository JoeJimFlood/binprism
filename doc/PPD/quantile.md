# binprism.PPD.quantile
**`PPD.quantile(p, tol = 1e-8, max_iter = 1000, n_interpolation_points = 4)`** <br />
Quantile function evaluated at a probability using the Newton-Raphson method

## Parameters
**p (numeric or array-like):** *Probability(ies) to evaluate the quantile function at* <br />
**tol (float):** *Tolerance for Newton-Raphson iterations* <br />
**max_iter (int):** *Maximum number of Newton-Raphson iterations* <br />
**n_interpolation_points (int):** *Number of interpolation points when determining initial guess*

## Returns
**theta (numeric or array-like):** *Quantile function evaluated at* `p`

## Example
```
>>> fs = bp.FourierSeries([-2, 0.2 + 0.3j, -0.7 - 0.4j, -0.1 - 0.15j])
>>> dist = bp.PPD(fs)
>>> p = np.linspace(0, 1, 250)[1:-1]
>>> plt.plot(p, dist.quantile(p), color = 'k')
>>> plt.xlim(0, 1)
>>> plt.grid(True)
>>> plt.show()
```
![alt text](QuantileExample.png "PPD.quantile() example")