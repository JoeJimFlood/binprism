from __future__ import division
import numpy as np
import sys
from numbers import Number
from math import factorial, pi

class FourierSeries:
    '''
    Fourier series representing real-valued periodic function

    Attributes
    ----------
    c (numpy.array):
        DC component as well as positive-indexed elements of Fourier series
    K (int):
        Number of component waves
    '''
    def __init__(self, c):
        self.c = np.array(c)
        self.K = len(c) - 1

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
        for k in range(2, self.K+1):
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
        Estimates the maximum of the Fourier series

        Parameters
        ----------
        N (int):
            Number of points in array to estimate with

        Returns
        -------
        max (float):
            Maximum value of function
        '''
        return self.eval(np.linspace(0, 2*pi, N, False)).max()

    def min(self, N = 1024):
        '''
        Estimates the minimum of the Fourier series

        Parameters
        ----------
        N (int):
            Number of points in array to estimate with

        Returns
        -------
        min (float):
            Minimum value of function
        '''
        return self.eval(np.linspace(0, 2*pi, N, False)).min()

    def copy(self):
        '''
        Creates a copy of the Fourier Series object

        Returns
        -------
        copy (spectranspo.FourierSeries):
            Copy of input Fourier Series
        '''
        return FourierSeries(self.c)

    def expand(self):
        self.c = np.append(self.c, np.conj(np.fliplr(np.reshape(self.c, (1, self.K+1))[:, 1:])[0]))

    def contract(self):
        self.c = self.c[:self.K+1]

    def power(self, n):
        '''
        Raises a Fourier Series to the n-th power using the convolution theorem
        
        Parameters
        ----------
        n (int):
            Power to raise Fourier series to

        Returns
        -------
        fs (spectranspo.FourierSeries):
            Fourier series raised to n-th power
        '''
        if n == 0:
            return FourierSeries([1])
        
        self.expand()
        result = np.fft.fftshift(self.c)
        coeff = result
        
        for i in range(1, n):
            result = np.convolve(result, coeff)
        
        result = np.fft.ifftshift(result)
        K = len(result)//2
        self.contract()
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

    def log(self, tol = 2**-23, max_iter = 1000):
        '''
        Finds the Fourier coefficients of the logarithm of the wave using a Taylor series. If any part of the wave is negative, an error will be raised.

        Parameters
        ----------
        tol (float):
            Tolerance for Taylor series approximation
        max_iter (int):
            Maximum number of Taylor series iterations
        '''
        if self.min() <= 0:
            raise ValueError('Cannot take logarithm of function with negative values')

        out = self - 1
        for n in range(2, max_iter + 1):
            change = ((self-1)**n)*(((-1)**(n+1))/n)
            out += change
            if np.linalg.norm(change.c, np.inf) < tol:
                break
        if n == max_iter:
            print('WARNING: Maximum number of iterations reached in Fourier series logarithm')

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
        for k in range(1, self.K+1):
            y += np.real(self.c[k]*np.exp(1j*k*x) + np.conj(self.c[k])*np.exp(-1j*k*x))
        return y

    def diff(self):
        '''
        Returns Fourier series of the derivative

        Returns
        -------
        derivative (spectranspo.FourierSeries):
            Differentiated Fourier series
        '''
        k = np.arange(self.K+1)
        return FourierSeries(self.c*1j*k)

    def antiderivative(self):
        '''
        Returns Fourier series of the nonlinear components of the Fourier series

        Returns
        -------
        antiderivative (spectranspo.FourierSeries):
            Fourier series of the nonlinear parts of the antiderivative
        '''
        k = np.arange(self.K+1) + np.array([1] + (self.K)*[0])
        ad_c = -self.c*1j/k
        ad_c[0] = 0
        return FourierSeries(ad_c)

    def integrate(self, a, b):
        '''
        Integrates the function from a to b

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
        return np.real(result)

    def shift(self, phi, inplace = True):
        '''
        Shifts a Fourier series by phase shift phi

        Parameters
        ----------
        phi (float):
            Angle to shift Fourier series by
        inplace (bool):
            Indicates whether or not to perform the operation in place

        Returns
        -------
        shifted_fourier_series (spectranspo.FourierSeries):
            Fourier series shifted by phi
        '''
        k = np.arange(self.K + 1)
        z = np.exp(-1j*phi*k)
        if inplace:
            self.c *= z
        else:
            return FourierSeries(self.c*z)