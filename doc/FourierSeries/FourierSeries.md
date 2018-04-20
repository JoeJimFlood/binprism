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
[antiderivative](antiderivative.md) <br/>
[copy](copy.md) <br/>
[diff](diff.md) <br/>
[eval](eval.md) <br/>
[exp](exp.md) <br/>
[integrate](integrate.md) <br/>
[log](log.md) <br/>
[max](max.md) <br/>
[min](min.md) <br/>
[shift](shift.md)
