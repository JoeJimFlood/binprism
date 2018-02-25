from .tools import sim
import numpy as np
from .FourierSeries import FourierSeries
from .MomentCalculator import MomentCalculator
from math import exp, log, pi, factorial as fac
from scipy.integrate import simps
from numbers import Number
from multiprocessing import Pool

class PPD:
    '''
    Periodic probability distribution defined by the Fourier coefficients of the log-pdf

    Parameters
    ----------
    log_pdf_coef (binprism.FourierSeries): Fourier series defining the log-pdf of the distribution (aka L)
    '''
    def __init__(self, log_pdf_coef):

        self.log_pdf_coef = log_pdf_coef
        init_area = self.log_pdf_coef.exp().integrate(0, 2*pi)
        self.log_pdf_coef[0] -= log(init_area) #Normalize so that area of one period is equal to one
        self.L = self.log_pdf_coef
        self.time_range = (0, 2*pi)
        self.m = MomentCalculator(self)

    def __repr__(self):
        return 'f(x) = exp({})'.format(self.log_pdf_coef)

    def pdf(self, theta):
        '''
        Evaluates the probability density function at theta

        Parameters
        ----------
        theta (numeric or array-like):
            Angle at which to evaluate the pdf

        Returns
        -------
        f (numeric or array-like):
            pdf evaluated at theta
        '''
        return np.exp(self.log_pdf_coef.eval(theta))

    def cdf(self, theta):
        '''
        Cummulative distribution function at theta

        Parameters
        ----------
        theta (numeric or array-like):
            Angle at which to evaluate the cdf

        Returns
        -------
        F (numeric or array-like):
            cdf evaluated at theta
        '''
        return self.log_pdf_coef.exp().integrate(0, theta)

    def quantile(self, p, tol = 1e-8, max_iter = 1000, n_interpolation_points = 4):
        '''
        Quantile function evaluated at a probability using the Newton-Raphson method

        Parameters
        ----------
        p (numeric or array-like):
            Probability(ies) to evaluate the quantile function at
        tol (float):
            Tolerance for Newton-Raphson iterations
        max_iter (int):
            Maximum number of Newton-Raphson iterations
        n_interpolation_points (int):
            Number of interpolation points when determining initial guess

        Returns
        -------
        theta (numeric or array-like):
            Quantile function evaluated at p
        '''
        try:
            assert p >= 0 and p <= 1, 'p must be between 0 and 1'
        except ValueError:
            assert min(p) >= 0 and max(p) <= 1, 'p must be between 0 and 1'

        theta = sim.get_initial_t(p, self, n_interpolation_points)
        for i in range(max_iter):
            change = (self.cdf(theta) - p)/self.pdf(theta)
            theta -= change
            if np.linalg.norm(change)/np.sqrt(len(theta)) < tol:
                break
        return theta

    def mean(self):
        '''
        Returns the mean angle of the distribution
        '''
        return np.angle(self.m[1])%(2*pi)

    def var(self):
        '''
        Returns the circular variance of the distribution
        '''
        return 1 - abs(self.m[1])

    def disp(self):
        ''''
        Returns the circular dispersion of the distribution
        '''
        (R1, R2) = abs(self.m[1:3])
        return (1 - R2)/(2*R1**2)

    #def sim(self, N, tol = 1e-8, max_iter = 1000, n_interpolation_points = 4):
    def sim(self, N, **kwargs):
        '''
        Simulates N points following the distribution by simulating N random values between 0 and 1 and then evaluating the quantile function

        N (int):
            Number of events to simulate
        **kwargs:
            Additional arguments for evaluating quantile function
        '''
        return self.quantile(np.random.random(N), **kwargs)