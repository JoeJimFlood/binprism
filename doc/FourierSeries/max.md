# binprism.FourierSeries.max
**`FourierSeries.max(N = 1024)`** <br/>
Estimates the maximum of the function represented by the Fourier series by evaluating at many equally-spaced points within a period and returning the maximum.
## Parameters
**N (int):** *Number of points to estimate maximum with*
## Returns
**max (float):** *Maximum of function represented by Fourier series*
```
>>> fs = bp.FourierSeries([1, 0.5, 0.5, 0.5]) #f(x) = 1 + cos(x) + cos(2x) + cos(3x)
>>> fs.max()
4.0
```
