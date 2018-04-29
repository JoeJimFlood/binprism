# binprism.FourierSeries.diff
**`FourierSeries.diff()`** <br />
Returns Fourier series of the derivative
## Returns
**derivative (binprism.FourierSeries):** *Differentiated Fourier series*
## Example
```
>>> fs = bp.FourierSeries([5, -4 + 3j, -2 - 1j])
>>> fs
5.0 + (-8.0)cos(x) + (-6.0)sin(x) + (-4.0)cos(2x) + (2.0)sin(2x)
>>> derivative = fs.diff()
>>> derivative
0.0 + (-6.0)cos(x) + (8.0)sin(x) + (4.0)cos(2x) + (8.0)sin(2x)
>>> x = np.linspace(0, 2*np.pi, 250)
>>> plt.plot(x, fs.eval(x), color = 'r', label = 'Fourier Series')
>>> plt.plot(x, derivative.eval(x), color = 'b', label = 'Derivative')
>>> plt.grid(True)
>>> plt.xlim(0, 2*np.pi)
>>> plt.legend(loc = 'best')
>>> plt.show()
```
