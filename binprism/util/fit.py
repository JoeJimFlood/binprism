import numpy as np
from math import pi
from ..core.FourierSeries import FourierSeries
from ..core.PPD import PPD
from ..core.Profile import Profile

from scipy.optimize import minimize

def fit(data, bins, n_harmonics, time_range, optimize = False, optimization_method = 'fmin', optimization_norm = 2, **optimization_args):
    '''
    Fits a profile to best match binned data by solving the linear system of equations described in the methodology section in the documentation.

    Parameters
    ----------
    data (array-like):
        Data to fit profile to match
    bins (array-like):
        Start times of each bin. The length must be the same as `data`
    n_harmonics (int):
        Maximum number of harmonics used in fitting the log-pdf of the underlying distribution
    time_range (tuple):
        Length-2 tuple indicating the values of time that map to 0 and 2-pi, respectively, in the underlying distribution
    optimize (bool):
        Boolean variable indicating whether or not to use a nonlinear optimization algorithm to better match the profile to the data
    optimization_method (str):
        Name of scipy.optimize method to use in nonlinear optimization
    optimization_norm (float):
        P-norm to minimize when comparing the input data to the profile
    optimization_args:
        Additional arguments for chosen optimization method

    Returns
    -------
    Profile (binprism.Profile):
        Profile fit from input data
    '''
    for b in bins:
        if b < time_range[0] or b >= time_range[1]:
            raise ValueError('Bin start times must be within time_range')

    assert len(bins) == len(data), 'Data and bins must have same length.'

    N = len(data)
    K = n_harmonics
    data = np.array(data).astype(float)
    bins = 2*pi*(np.array(bins) - time_range[0])/(time_range[1] - time_range[0])
    bins = np.append(bins, 2*pi).astype(float)
    widths = np.diff(bins)
    total = data.sum()
    props = data / total

    #Create design matrix for OLS
    X = np.zeros((N, 2*K+1), np.complex)
    for i in range(N):
        a = bins[i]
        b = bins[i+1]
        X[i, 0] = b - a
        for k in range(1, K+1):
            X[i, k] = -1j/k*(np.exp(1j*k*b) - np.exp(1j*k*a))
            X[i, -k] = np.conj(X[i, k])

    #Comute best coefficients via ordinary least squares regression
    y = widths*np.log(props/widths)
    XTX = np.dot(X.T, X)
    XTy = np.dot(X.T, y)
    c = np.linalg.solve(XTX, XTy)[:K+1]

    #Run nonlinear optimization if desired
    if optimize:
        def error(params):
            coefs = params[:K+1] + np.hstack((0, 1j*params[K+1:]))
            fs = FourierSeries(coefs)
            dist = PPD(fs)
            return np.linalg.norm(dist.cdf(bins[1:]) - dist.cdf(bins[:-1]) - data/data.sum(), optimization_norm)
        init_coefs = np.hstack((np.real(c), np.imag(c[1:])))
        #opt_coefs = getattr(scipy.optimize, optimization_method)(error, init_coefs, **optimization_args)
        opt_coefs = minimize(error, init_coefs, **optimization_args)
        c = opt_coefs['x'][:K+1] + np.hstack((0, 1j*opt_coefs['x'][K+1:]))

    #Create distribution
    fs = FourierSeries(c)
    dist = PPD(fs)
    return Profile(dist, total, time_range)