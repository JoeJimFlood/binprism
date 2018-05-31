from __future__ import division
import numpy as np
import sys
from numbers import Number
from math import factorial, pi

class FourierSeries:
    '''
    Fourier series representing real-valued periodic function

    A `FourierSeries` is the most basic class in the BinPrism package.
    It contains the coefficients of a Fourier series representing a real-valued periodic function. The function is of the form:
    `coef[0] + coef[1]*exp(1j*x) + np.conj(coef[1])*exp(-1j*x) + coef[2]*exp(2j*x) + np.conj(coef[2])*exp(-2j*x) + ...`
    `= coef[0] + 2*np.real(coef[1])*cos(x) - 2*np.imag(coef[1])*sin(x) + 2*np.real(coef[2])*cos(2*x) - 2*np.imag(coef[2])*sin(2*x) + ...`
    
    Parameters
    ----------
    coef (numpy.array):
        Zero- and positive-indexed Fourier coefficients

    Attributes
    ----------
    coef (numpy.array):
        Zero- and positive-indexed Fourier coefficients
    n_harmonics (int):
        Number of harmonics represented by Fourier series (len(coef) - 1)
    c:
        Alias of coef
    K:
        Alias of n_harmonics
    '''
    def __init__(self, coef):
        self.coef = np.array(coef).astype(complex)
        self.c = self.coef
        self.n_harmonics = len(coef) - 1
        self.K = self.n_harmonics
        
    def __getitem__(self, key):
        return self.c[key]

    def __setitem__(self, key, value):
        self.c[key] = value

    def __len__(self):
        return len(self.c)

    def __str__(self):
        if len(self) == 1:
            return str(self[0])
        out = '{0} + ({1})cos(x) + ({2})sin(x)'.format(np.real(self[0]), 2*np.real(self[1]), -2*np.imag(self[1]))
        for k in range(2, self.n_harmonics+1):
            out += ' + ({0})cos({1}x) + ({2})sin({3}x)'.format(2*np.real(self[k]), k, -2*np.imag(self[k]), k)
        return out

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, Number):
            return FourierSeries(self.c + np.append(np.array([other]), np.zeros_like(self.c)[1:]))
        elif isinstance(other, FourierSeries):
            if len(self.c) == len(other.c):
                return FourierSeries(self.c + other.c)
            elif len(self.c) > len(other.c):
                return FourierSeries(self.c + np.concatenate((other.c, np.zeros(len(self.c) - len(other.c), np.complex))))
            else:
                return FourierSeries(np.concatenate((self.c, np.zeros(len(other.c) - len(self.c), np.complex))) + other.c) 
        else:
            raise TypeError('Invalid type for Fourier Series addition')

    def __neg__(self):
        return FourierSeries(-self.c)

    def __sub__(self, other):
        if isinstance(other, Number):
            return FourierSeries(self.c + np.append(np.array([-other]), np.zeros_like(self.c)[1:]))
        elif isinstance(other, FourierSeries):
            return FourierSeries(self.c + -other.c)
        else:
            raise TypeError('Invalid type for Fourier Series subtraction')

    def __mul__(self, other):
        if isinstance(other, Number):
            return FourierSeries(other*self.c)
        elif isinstance(other, FourierSeries):
            self_c = list(np.conj(self.c[1:]))
            other_c = list(np.conj(other.c[1:]))
            self_c.reverse()
            other_c.reverse()
            self_c = np.array(self_c + list(self.c))
            other_c = np.array(other_c + list(other.c))
            product_c = np.convolve(self_c, other_c)
            K = int(len(product_c) // 2 - 1)
            return FourierSeries(product_c[K+1:])
        else:
            raise TypeError('Invalid type for Fourier Series multiplication')

    def __truediv__(self, other):
        if isinstance(other, Number):
            return FourierSeries(self.c/other)
        else:
            raise TypeError('Invalid type for Fourier Series division')

    def __pow__(self, n):
        return self.power(n)

    def max(self, N = 1024):
        '''
        Estimates the maximum of the function represented by the Fourier series by evaluating at many equally-spaced points within a period and returning the maximum.

        Parameters
        ----------
        N (int):
            Number of points in array to estimate with

        Returns
        -------
        max (float):
            Maximum of function represented by Fourier series
        '''
        return self.eval(np.linspace(0, 2*pi, N, False)).max()

    def min(self, N = 1024):
        '''
        Estimates the minimum of the function represented by the Fourier series by evaluating at many equally-spaced points within a period and returning the minimum.

        Parameters
        ----------
        N (int):
            Number of points in array to estimate with

        Returns
        -------
        min (float):
            Minimum of function represented by Fourier series
        '''
        return self.eval(np.linspace(0, 2*pi, N, False)).min()

    def copy(self):
        '''
        Creates a copy of the Fourier series object so that the original Fourier series is not changed when its copies are edited.

        Returns
        -------
        copy (binprism.FourierSeries):
            Copy of input Fourier Series
        '''
        return FourierSeries(self.c)

    def _expand(self):
        self.c = np.append(self.c, np.conj(np.fliplr(np.reshape(self.c, (1, self.n_harmonics+1))[:, 1:])[0]))

    def _contract(self):
        self.c = self.c[:self.n_harmonics+1]

    def power(self, n):
        '''
        Raises a Fourier Series to the n-th power using the convolution theorem
        
        Parameters
        ----------
        n (int):
            Power to raise Fourier series to

        Returns
        -------
        fs (binprism.FourierSeries):
            Fourier series raised to n-th power
        '''
        if n == 0:
            return FourierSeries([1])
        
        self._expand()
        result = np.fft.fftshift(self.c)
        coeff = result
        
        for i in range(1, n):
            result = np.convolve(result, coeff)
        
        result = np.fft.ifftshift(result)
        K = len(result)//2
        self._contract()
        return FourierSeries(result[:K+1])

    def exp(self, tol = 2**-23, max_iter = 1000):
        '''
        Finds the Fourier coefficients of the exponentiated wave using a Taylor series

        Parameters
        ----------
        tol (float):
            Tolerance for Taylor series approximation
        max_iter (int):
            Maximum number of Taylor series iterations

        Returns
        -------
        out (binprism.FourierSeries):
            Exponentiated Fourier series
        '''
        out = FourierSeries([1])
        for n in range(1, max_iter):
            change = (self**n) / (factorial(n))
            out += change
            if np.linalg.norm(change.c, np.inf) < tol:
                break
        if n == max_iter - 1:
            print('WARNING: Maximum number of iterations reached in Fourier series exponentiation')

        return out

    def eval(self, x):
        '''
        Evaluates the Fourier series at the value(s) x

        Parameters
        ----------
        x (numeric or array-like):
            X-value(s) of point(s) to evaluate the Fourier series

        Returns
        -------
        y (numeric or array-like):
            Y-value(s) of Fourier series evaluated at x
        '''
        y = np.real(self.c[0])*np.ones_like(x)
        for k in range(1, self.n_harmonics+1):
            y += np.real(self.c[k]*np.exp(1j*k*x) + np.conj(self.c[k])*np.exp(-1j*k*x))
        return y

    def diff(self):
        '''
        Returns Fourier series of the derivative

        Returns
        -------
        derivative (binprism.FourierSeries):
            Differentiated Fourier series
        '''
        k = np.arange(self.n_harmonics+1)
        return FourierSeries(self.c*1j*k)

    def antiderivative(self):
        '''
        Returns Fourier series of the nonlinear components of the Fourier series

        Returns
        -------
        antiderivative (binprism.FourierSeries):
            Fourier series of the nonlinear parts of the antiderivative
        '''
        k = np.arange(self.n_harmonics+1) + np.array([1] + (self.n_harmonics)*[0])
        ad_c = -self.c*1j/k
        ad_c[0] = 0
        return FourierSeries(ad_c)

    def integrate(self, a, b):
        '''
        Integrates the function represented by the Fourier series from `a` to `b`.

        Parameters
        ----------
        a (numeric or array-like):
            Start of integration
        b (numeric or array-like):
            End of integration

        Returns
        -------
        result (numeric or numpy.array):
            integration result
        '''
        result = self.c[0]*(b - a)
        antiderivative = self.antiderivative()
        result += (antiderivative.eval(b) - antiderivative.eval(a))
        try:
            len(np.real(result))
            return np.real(result)
        except TypeError:
            return float(np.real(result))

    def shift(self, phi, inplace = True):
        '''
        Shifts a Fourier series by phase shift `phi`

        Parameters
        ----------
        phi (float):
            Phase shift to shift Fourier series by
        inplace (bool):
            Indicates whether or not to perform the operation in place

        Returns
        -------
        shifted_fourier_series (binprism.FourierSeries):
            Fourier series shifted by `phi`
        '''
        k = np.arange(self.n_harmonics + 1)
        z = np.exp(-1j*phi*k)
        if inplace:
            self.c *= z
        else:
            return FourierSeries(self.c*z)