# BinPrism
Tools for fitting linear combinations of continuous basis functions to match binned data.

Often, data from continuous variables are binned. When bins are too large, one cannot directly draw conclusions about smaller bins. This could be resolved by using smaller bins for more re-aggregation possiblities, but that makes the data more susceptible to noise. BinPrism resolves both of these issues by fitting [Generalized Fourier Series](https://en.wikipedia.org/wiki/Generalized_Fourier_series) to match the bins. This is done by first selecting an appropriate basis for the data, and then estimating coefficients that minimize the root-mean squared error between re-aggregated data and the actual data. At the moment, this can only be done for data on periodic domains (such as daily or yearly patterns), but in the future it is hoped that more domains will be supported.

## Methodology
Random events occur at different times following a profile P(t) with period T. Dividint the profile by the total number of events results in a periodic probability density function (pdf):

<a href="https://www.codecogs.com/eqnedit.php?latex=f(t)\equiv\frac{P(t)}{P_{tot}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(t)\equiv\frac{P(t)}{P_{tot}}" title="f(t)\equiv\frac{P(t)}{P_{tot}}" /></a>
