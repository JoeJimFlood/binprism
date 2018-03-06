# BinPrism
Tools for fitting linear combinations of continuous basis functions to match binned data.

Often, data from continuous variables are binned. When bins are too large, one cannot directly draw conclusions about smaller bins. This could be resolved by using smaller bins for more re-aggregation possiblities, but that makes the data more susceptible to noise. BinPrism resolves both of these issues by fitting [Generalized Fourier Series](https://en.wikipedia.org/wiki/Generalized_Fourier_series) to match the bins. This is done by first selecting an appropriate basis for the data, and then estimating coefficients that minimize the root-mean squared error between re-aggregated data and the actual data. At the moment, this can only be done for data on periodic domains (such as daily or yearly patterns), but in the future it is hoped that more domains will be supported.

## Methodology
Random events occur at different times following a profile P(t) with period T. Dividing the profile by the total number of events results in a periodic probability density function (pdf):
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=f(t)\equiv\frac{P(t)}{P_{tot}}" target="_blank"><img      src="https://latex.codecogs.com/gif.latex?f(t)\equiv\frac{P(t)}{P_{tot}}" title="f(t)\equiv\frac{P(t)}{P_{tot}}" /></a>
</p>
Because the pdf is periodic, it can be expanded into a Fourier series. However, low-frequency approximations of the pdf can result in periods with negative probabilities, violating one of the properties of pdfs. This can be resolved by performing the Fourier series expansion on the logarithm of the pdf, or the log-pdf. Because the pdf is periodic, the log-pdf must be as well.
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=l(t)\equiv\ln{f(t)}=\sum_{k=-\infty}^{\infty}L_ke^{\frac{2\pi&space;kt}{T}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?l(t)\equiv\ln{f(t)}=\sum_{k=-\infty}^{\infty}L_ke^{\frac{2\pi&space;kt}{T}}" title="l(t)\equiv\ln{f(t)}=\sum_{k=-\infty}^{\infty}L_ke^{\frac{2\pi kt}{T}}" /></a>
</p>
Because Fourier series converge, they can be sufficiently approximated by a finite number of terms:
<p align="center">
  l(t)\approx\sum_{k=-K}^{K}L_ke^{\frac{2\pi kt}{T}}
</p>
