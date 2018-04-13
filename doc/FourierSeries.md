# FourierSeries
**`binprism.FourierSeries(coef)`** <br />
*coef (numpy.array): Zero- and positive-indexed Fourier coefficients* <br />

A `FourierSeries` is the most basic class in the BinPrism package. It contains the coefficients of a Fourier series representing a real-valued periodic function.

## Attributes
*coef (numpy.array): Zero- and positive-indexed Fourier coefficients* <br />
*n_harmonics (int): Number of harmonics represented by Fourier series (*`len(coef) - 1`*)* <br />
*c: Alias of* `coef` <br />
*K: Alias of* `n_harmonics` <br/>

## Methods

### max
**`binprism.FourierSeries.max(N = 1024)`**
Estimates the maximum of the function represented by the Fourier series by evaluating at many equally-spaced points within a period and returning the maximum.
#### Parameters
*N (int): Number of points to estimate maximum with*
#### Returns
*max (float): Maximum of function represented by Fourier series*
