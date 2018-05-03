# binprism.PPD.pdf
**`PPD.pdf(theta)`**
Evaluates the probability distribution function at `theta`

## Parameters
**theta (numeric or array-like):** *Angle at which to evaluate the PDF*

## Returns
**f (numeric or array-like):** *PDF evaluated at* `theta`

## Example
```
>>> fs = bp.FourierSeries([-2, 0.5j, 0.3 + 0.4j, -0.2 + 0.15j])
>>> dist = bp.PPD(fs)
>>> theta = np.linspace(0, 2*np.pi, 250)
>>> plt.plot(theta, dist.pdf(theta), color = 'k')
>>> plt.grid(True)
>>> plt.xlim(0, 2*np.pi)
>>> plt.xlabel(r'$\theta$')
>>> plt.ylabel(r'$f(\theta)$')
>>> plt.show()
```
![alt text](PDFExample.png "PPD.pdf() example")
