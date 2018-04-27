# binprism.FourierSeries
**`binprism.FourierSeries(coef)`** <br />
**coef (numpy.array)**: *Zero- and positive-indexed Fourier coefficients* <br />

A `FourierSeries` is the most basic class in the BinPrism package. It contains the coefficients of a Fourier series representing a real-valued periodic function. The function is of the form: <br />
`coef[0] + coef[1]*exp(1j*x) + np.conj(coef[1])*exp(-1j*x) + coef[2]*exp(2j*x) + np.conj(coef[2])*exp(-2j*x) + ...` <br />
`= coef[0] + 2*np.real(coef[1])*cos(x) - 2*np.imag(coef[1])*sin(x) + 2*np.real(coef[2])*cos(2*x) - 2*np.imag(coef[2])*sin(2*x) + ...`

## Attributes
**coef (numpy.array):** *Zero- and positive-indexed Fourier coefficients* <br />
**n_harmonics (int):** *Number of harmonics represented by Fourier series (*`len(coef) - 1`*)* <br />
**c:** *Alias of* `coef` <br />
**K:** *Alias of* `n_harmonics` <br/>

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

## Examples
```
>>> import binprism as bp
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> fs1 = bp.FourierSeries([1, 0.5]) #f(x) = 1 + cos(x)
>>> fs2 = bp.FourierSeries([1, -0.5j]) #f(x) = 1 + sin(x)
>>> fs3 = bp.FourierSeries([1.5, -0.25 + 0.25j, 0.3 + 0.4j]) #f(x) = 1.5 - 0.5*cos(x) - 0.5*sin(x) + 0.6*cos(2x) - 0.8*sin(2x)
>>> x = np.linspace(0, 2*np.pi, 250)
>>> plt.plot(x, fs1.eval(x), color = 'r', label = str(fs1))
>>> plt.plot(x, fs2.eval(x), color = 'b', label = str(fs2))
>>> plt.plot(x, fs3.eval(x), color = 'm', label = str(fs3))
>>> plt.grid(True)
>>> plt.show()
```
