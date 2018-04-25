# binprism.PPD
***`binprism.PPD(log_pdf_coef)`*** <br />
*log_pdf_coef (binprism.FourierSeries): Fourier Series of the distribution's log-pdf* <br />

The `PPD` class is a periodic probability distribution defined by the Fourier coefficients of its log-pdf. When created, the coefficients of the log-pdf are adjusted so the area under one period of the `PPD` is equal to one.

## Attributes
*log_pdf_coef (binprism.FourierSeries): Fourier Series of the distribution's log-pdf* <br />
*L: Alias of* `log_pdf_coef` <br />
*moments (binprism.MomentCalculator): Circular moments of the distribution* <br/>
*m: Alias of* `moments`

## Methods
cdf <br />
disp <br />
mean <br />
pdf <br />
quantile <br />
sim <br />
var
