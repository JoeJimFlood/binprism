from numpy import conj
from math import pi

class MomentCalculator:
    '''
    Calculates circular moments of periodic probability distributions.

    Parameters
    ----------
    dist (binprism.PPD):
        Distribution to calculate moments of
    '''
    def __init__(self, dist):
        self.dist = dist

    def __getitem__(self, n):
        moments = 2*pi*conj(self.dist.L.exp().c)
        try:
            return moments[n]
        except IndexError:
            return 0j