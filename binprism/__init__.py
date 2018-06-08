'''
binprism

Tools for fitting linear combinations of continuous basis functions to match binned data.

Often, data from continuous variables are placed into discrete bins.
BinPrism fits continuous profiles to match these bins, allowing for the ability to
    *Produce clean visualizations
    *Estimate results from different bin sizes
    *Simulate data following a distribution matching the original data.
    
 Presently, BinPrism only works for periodic data (such as daily or yearly patterns),
 but it is hoped that in the future more domains will be supported.
'''
from .version import *
from .core import *
from .util import *

def dinosaur():
    print(' _____\n/  o  \\\n>      \\\n\\____   \\\n     \\   \\\n      \\   \\____________\n      |                \\\n      |                \\\\\n      |     ______     |\\\\\n      |    /      \\    | \\|\n      |    |      |    |\n      |____|      |____|\n\n         DINOSAUR!\n')
