# binprism.FourierSeries.min
**`FourierSeries.min(N = 1024)`** <br/>
Estimates the minimum of the function represented by the Fourier series by evaluating at many equally-spaced points within a period and returning the minimum.
## Parameters
**N (int):** *Number of points to estimate minimum with*
## Returns
**min (float):** *Minimum of function represented by Fourier series*
```
>>> fs = bp.FourierSeries([-1, -0.5, -0.5, -0.5) #f(x) = -1 - cos(x) - cos(2x) - cos(3x)
>>> fs.min()
-4.0
```