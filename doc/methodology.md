# Methodology
Random events occur at different times following a profile P(t) with period T. Dividing the profile by the total number of events results in a periodic probability density function (pdf):
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=f(t)\equiv\frac{P(t)}{P_{tot}}" target="_blank"><img      src="https://latex.codecogs.com/gif.latex?f(t)\equiv\frac{P(t)}{P_{tot}}" title="f(t)\equiv\frac{P(t)}{P_{tot}}" /></a>
</p>
Because the pdf is periodic, it can be expanded into a Fourier series. However, low-frequency approximations of the pdf can result in periods with negative probabilities, violating one of the properties of pdfs. This can be resolved by performing the Fourier series expansion on the logarithm of the pdf, or the log-pdf. Because the pdf is periodic, the log-pdf must be as well.
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=l(t)\equiv\ln{f(t)}=\sum_{k=-\infty}^{\infty}L_ke^{i\frac{2\pi&space;kt}{T}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?l(t)\equiv\ln{f(t)}=\sum_{k=-\infty}^{\infty}L_ke^{i\frac{2\pi&space;kt}{T}}" title="l(t)\equiv\ln{f(t)}=\sum_{k=-\infty}^{\infty}L_ke^{i\frac{2\pi kt}{T}}" /></a>
</p>
Because Fourier series converge, they can be sufficiently approximated by a finite number of terms:
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=l(t)\approx\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?l(t)\approx\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}}" title="l(t)\approx\sum_{k=-K}^{K}L_ke^{i\frac{2\pi kt}{T}}" /></a>
</p>
The proportion, p, of events between times t<sub>a</sub> and t<sub>b</sub> can be obtained by integrating the exponentiated log-pdf from t<sub>a</sub> to t<sub>b</sub>:
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=p\equiv\int_{t_a}^{t_b}f(t)dt=\int_{t_a}^{t_b}\exp(l(t))dt\approx\int_{t_a}^{t_b}\exp(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}})dt" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p\equiv\int_{t_a}^{t_b}f(t)dt=\int_{t_a}^{t_b}\exp(l(t))dt\approx\int_{t_a}^{t_b}\exp(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}})dt" title="p\equiv\int_{t_a}^{t_b}f(t)dt=\int_{t_a}^{t_b}\exp(l(t))dt\approx\int_{t_a}^{t_b}\exp(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi kt}{T}})dt" /></a>
</p>
If one has the proportion of events from multiple time periods, then the Fourier coefficients L<sub>k</sub> that minimize the error can be estimated using a non-linear optimization algorithm. However, such algorithms can be very time consuming. Fortunately, a solution can be quickly approximated by linearizing the problem using Taylor series. To start, the integrand in the previous equation can be expanded in the following way:
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=p\approx\int_{t_a}^{t_b}(\sum_{n=0}^{\infty}\frac{(\sum_{k=-K}^{K}L_k\exp(i\frac{2\pi&space;kt}{T}))^n}{n!})dt" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p\approx\int_{t_a}^{t_b}(\sum_{n=0}^{\infty}\frac{(\sum_{k=-K}^{K}L_k\exp(i\frac{2\pi&space;kt}{T}))^n}{n!})dt" title="p\approx\int_{t_a}^{t_b}(\sum_{n=0}^{\infty}\frac{(\sum_{k=-K}^{K}L_k\exp(i\frac{2\pi kt}{T}))^n}{n!})dt" /></a>
  <a href="https://www.codecogs.com/eqnedit.php?latex==\int_{t_a}^{t_b}dt&plus;\int_{t_a}^{t_b}(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}})dt&plus;\sum_{n=2}^{\infty}\frac{1}{n!}\int_{t_a}^{t_b}(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}})^n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=\int_{t_a}^{t_b}dt&plus;\int_{t_a}^{t_b}(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}})dt&plus;\sum_{n=2}^{\infty}\frac{1}{n!}\int_{t_a}^{t_b}(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}})^n" title="=\int_{t_a}^{t_b}dt+\int_{t_a}^{t_b}(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi kt}{T}})dt+\sum_{n=2}^{\infty}\frac{1}{n!}\int_{t_a}^{t_b}(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi kt}{T}})^n" /></a>
  <a href="https://www.codecogs.com/eqnedit.php?latex=\approx&space;t_b-t_a&plus;\int_{t_b}^{t_a}(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}})dt" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\approx&space;t_b-t_a&plus;\int_{t_b}^{t_a}(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi&space;kt}{T}})dt" title="\approx t_b-t_a+\int_{t_b}^{t_a}(\sum_{k=-K}^{K}L_ke^{i\frac{2\pi kt}{T}})dt" /></a>
  <a href="https://www.codecogs.com/eqnedit.php?latex==t_b-t_a&plus;\sum_{k=-K}^{K}\int_{t_a}^{t_b}L_ke^{i\frac{2\pi&space;kt}{T}}dt" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=t_b-t_a&plus;\sum_{k=-K}^{K}\int_{t_a}^{t_b}L_ke^{i\frac{2\pi&space;kt}{T}}dt" title="=t_b-t_a+\sum_{k=-K}^{K}\int_{t_a}^{t_b}L_ke^{i\frac{2\pi kt}{T}}dt" /></a>
  <a href="https://www.codecogs.com/eqnedit.php?latex==t_b-t_a&plus;L_0(t_b-t_a)&plus;\sum_{k=1}^{K}(-i\frac{L_k}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&plus;i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi&space;kt_b}{T}}-e^{-i\frac{2\pi&space;kt_a}{T}})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=t_b-t_a&plus;L_0(t_b-t_a)&plus;\sum_{k=1}^{K}(-i\frac{L_k}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&plus;i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi&space;kt_b}{T}}-e^{-i\frac{2\pi&space;kt_a}{T}})" title="=t_b-t_a+L_0(t_b-t_a)+\sum_{k=1}^{K}(-i\frac{L_k}{k}(e^{i\frac{2\pi kt_b}{T}}-e^{i\frac{2\pi kt_a}{T}})+i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi kt_b}{T}}-e^{-i\frac{2\pi kt_a}{T}})" /></a>
</p>
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=ln(p)=ln(p_0)&plus;\sum_{m=1}^{\infty}(-1)^{m&plus;1}\frac{(p-p_0)^m}{p_0^m}\approx&space;ln(p_0)&plus;\frac{p-p_0}{p_0}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?ln(p)=ln(p_0)&plus;\sum_{m=1}^{\infty}(-1)^{m&plus;1}\frac{(p-p_0)^m}{p_0^m}\approx&space;ln(p_0)&plus;\frac{p-p_0}{p_0}" title="ln(p)=ln(p_0)+\sum_{m=1}^{\infty}(-1)^{m+1}\frac{(p-p_0)^m}{p_0^m}\approx ln(p_0)+\frac{p-p_0}{p_0}" /></a>
</p>
Plugging the exponential series expansion into the logarithm series expansion (and replacing t<sub>b</sub>-t<sub>a</sub> with &#916t) yields:
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\ln(p)\approx&space;\ln(p_0)&plus;\frac{1}{p_0}(\Delta&space;t&plus;L_0\Delta&space;t&plus;\sum_{k=1}^{K}-i\frac{L_k}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&plus;i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi&space;kt_b}{T}}-e^{-i\frac{2\pi&space;kt_a}{T}})-p_0)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\ln(p)\approx&space;\ln(p_0)&plus;\frac{1}{p_0}(\Delta&space;t&plus;L_0\Delta&space;t&plus;\sum_{k=1}^{K}-i\frac{L_k}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&plus;i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi&space;kt_b}{T}}-e^{-i\frac{2\pi&space;kt_a}{T}})-p_0)" title="\ln(p)\approx \ln(p_0)+\frac{1}{p_0}(\Delta t+L_0\Delta t+\sum_{k=1}^{K}-i\frac{L_k}{k}(e^{i\frac{2\pi kt_b}{T}}-e^{i\frac{2\pi kt_a}{T}})+i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi kt_b}{T}}-e^{-i\frac{2\pi kt_a}{T}})-p_0)" /></a>
</p>
Rearranging this then results in the following approximation:
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=p_0(\ln(p)-\ln(p_0)))-\Delta&space;t-p_0\approx&space;L_0\Delta&space;t&plus;\sum_{k=1}^{K}-i\frac{L_k}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&plus;i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi&space;kt_b}{T}}-e^{-i\frac{2\pi&space;kt_a}{T}})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_0(\ln(p)-\ln(p_0)))-\Delta&space;t-p_0\approx&space;L_0\Delta&space;t&plus;\sum_{k=1}^{K}-i\frac{L_k}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&plus;i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi&space;kt_b}{T}}-e^{-i\frac{2\pi&space;kt_a}{T}})" title="p_0(\ln(p)-\ln(p_0)))-\Delta t-p_0\approx L_0\Delta t+\sum_{k=1}^{K}-i\frac{L_k}{k}(e^{i\frac{2\pi kt_b}{T}}-e^{i\frac{2\pi kt_a}{T}})+i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi kt_b}{T}}-e^{-i\frac{2\pi kt_a}{T}})" /></a>
</p>
Substituting p<sub>0</sub> with &#916t further simplifies the approximation.
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=p_0(\ln(p)-\ln(\Delta&space;t)))-\Delta&space;t-\Delta&space;t=p_0\ln(\frac{p}{\Delta&space;t})\approx&space;L_0\Delta&space;t&plus;\sum_{k=1}^{K}-i\frac{L_k}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&plus;i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi&space;kt_b}{T}}-e^{-i\frac{2\pi&space;kt_a}{T}})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_0(\ln(p)-\ln(\Delta&space;t)))-\Delta&space;t-\Delta&space;t=p_0\ln(\frac{p}{\Delta&space;t})\approx&space;L_0\Delta&space;t&plus;\sum_{k=1}^{K}-i\frac{L_k}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&plus;i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi&space;kt_b}{T}}-e^{-i\frac{2\pi&space;kt_a}{T}})" title="p_0(\ln(p)-\ln(\Delta t)))-\Delta t-\Delta t=p_0\ln(\frac{p}{\Delta t})\approx L_0\Delta t+\sum_{k=1}^{K}-i\frac{L_k}{k}(e^{i\frac{2\pi kt_b}{T}}-e^{i\frac{2\pi kt_a}{T}})+i\frac{\bar{L_k}}{k}(e^{-i\frac{2\pi kt_b}{T}}-e^{-i\frac{2\pi kt_a}{T}})" /></a>
</p>
The right side of the previous equation can be expressed as a matrix product between two vectors:
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\Delta&space;t\ln(\frac{p}{\Delta&space;t})\approx\textbf{xl}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\Delta&space;t\ln(\frac{p}{\Delta&space;t})\approx\textbf{xl}" title="\Delta t\ln(\frac{p}{\Delta t})\approx\textbf{xl}" /></a>
</p>
<p align="center">  
  <a href="https://www.codecogs.com/eqnedit.php?latex=\textbf{x}_k=\left\{\begin{matrix}&space;\Delta&space;t&space;&&space;k=0\\&space;\frac{i}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&space;&&space;k\ne0&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textbf{x}_k=\left\{\begin{matrix}&space;\Delta&space;t&space;&&space;k=0\\&space;\frac{i}{k}(e^{i\frac{2\pi&space;kt_b}{T}}-e^{i\frac{2\pi&space;kt_a}{T}})&space;&&space;k\ne0&space;\end{matrix}\right." title="\textbf{x}_k=\left\{\begin{matrix} \Delta t & k=0\\ \frac{i}{k}(e^{i\frac{2\pi kt_b}{T}}-e^{i\frac{2\pi kt_a}{T}}) & k\ne0 \end{matrix}\right." /></a>  
</p>
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\textbf{l}_k=L_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textbf{l}_k=L_k" title="\textbf{l}_k=L_k" /></a>
</p>
If N time periods are used, then the previous equation can be arranged into a system of linear equations.
<p align="center">
  <a href="https://www.codecogs.com/eqnedit.php?latex=\textbf{Xl}\equiv\begin{pmatrix}&space;\textbf{x}_1\\&space;\textbf{x}_2\\&space;\vdots&space;\\&space;\textbf{x}_N&space;\end{pmatrix}\textbf{l}\approx\begin{pmatrix}&space;\Delta&space;t_1\ln(\frac{p_1}{\Delta&space;t_1})\\&space;\Delta&space;t_2\ln(\frac{p_2}{\Delta&space;t_2})\\&space;\vdots&space;\\&space;\Delta&space;t_N\ln(\frac{p_N}{\Delta&space;t_N})&space;\end{pmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\textbf{Xl}\equiv\begin{pmatrix}&space;\textbf{x}_1\\&space;\textbf{x}_2\\&space;\vdots&space;\\&space;\textbf{x}_N&space;\end{pmatrix}\textbf{l}\approx\begin{pmatrix}&space;\Delta&space;t_1\ln(\frac{p_1}{\Delta&space;t_1})\\&space;\Delta&space;t_2\ln(\frac{p_2}{\Delta&space;t_2})\\&space;\vdots&space;\\&space;\Delta&space;t_N\ln(\frac{p_N}{\Delta&space;t_N})&space;\end{pmatrix}" title="\textbf{Xl}\equiv\begin{pmatrix} \textbf{x}_1\\ \textbf{x}_2\\ \vdots \\ \textbf{x}_N \end{pmatrix}\textbf{l}\approx\begin{pmatrix} \Delta t_1\ln(\frac{p_1}{\Delta t_1})\\ \Delta t_2\ln(\frac{p_2}{\Delta t_2})\\ \vdots \\ \Delta t_N\ln(\frac{p_N}{\Delta t_N}) \end{pmatrix}" /></a>
</p>
If N=2K+1, then the values of L<sub>k</sub> can be solved for directly. However, if N>2K+1, then they can be found using ordinary least squares regression.