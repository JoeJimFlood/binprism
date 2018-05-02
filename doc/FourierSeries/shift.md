# binprism.FourierSeries.shift
**`FourierSeries.shift(phi, inplace = True)`** <br />
Shifts a Fourier series by phase shift `phi`
## Parameters
**phi (numeric):** *Phase shift to shift Fourier series by* <br />
**inplace (bool):** *Indicates whether or not to perform the operation in place*
## Returns
**shifted_fourier_series (binprism.FourierSeries):** *Fourier series shifted by* `phi`
## Example
```
>>> fs = bp.FourierSeries([0, -1 + 2j, -0.3 - 0.4j, 0.1 + 0.25j])
>>> x = np.linspace(0, 2*np.pi, 250)
>>> plt.plot(x, fs.eval(x), color = 'b', label = 'Original')
>>> fs.shift(np.pi/2)
>>> plt.plot(x, fs.eval(x), color = 'm', label = 'Shifted $\pi/2$')
>>> fs.shift(np.pi/2)
>>> plt.plot(x, fs.eval(x), color = 'r', label = 'Shifted $\pi$')
>>> fs.shift(np.pi/2)
>>> plt.plot(x, fs.eval(x), color = 'y', label = 'Shifted $3\pi/2$')
>>> plt.grid(True)
>>> plt.xlim(0, 2*np.pi)
>>> plt.legend(loc = 'best')
>>> plt.show()
```
![alt text](ShiftExample.png "FourierSeries.shift() Example")