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
[antiderivative](antiderivative.md)
[copy](copy.md)
[diff](diff.md)
[eval](eval.md)
[exp](exp.md)
[integrate](integrate.md)
[log](log.md)
[max](max.md)
[min](min.md)
[shift](shift.md)
