from numpy import conj
from math import pi

class MomentCalculator:
    '''
    Calculates circular moments of periodic probability distributions.

    The `MomentCalculator` class is used to calculate circular moments of its associated periodic probability distribution object.
    The n-th circular moment is calculated by calling `MomentCalculator[n]`.

    Parameters
    ----------
    dist (binprism.PPD):
        Distribution to calculate moments of

    Attributes
    ----------
    dist (binprism.PPD):
        Distribution to calculate moments of
    '''
    def __init__(self, dist):
        self.dist = dist

    def __getitem__(self, n):
        moments = 2*pi*conj(self.dist.log_pdf_coef.exp().c)
        try:
            return moments[n]
        except IndexError:
            return 0j