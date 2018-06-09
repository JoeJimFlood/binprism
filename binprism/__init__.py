'''
binprism

Tools for fitting linear combinations of continuous basis functions to match binned data.

Often, data from continuous variables are placed into discrete bins.
BinPrism fits continuous profiles to match these bins, allowing for the ability to
    *Produce clean visualizations
    *Re-aggregate data into differently-sized bins
    *Simulate random values following a continuous distribution matching the original data

Like a prism separating light into different colors, BinPrism takes in binned data and separates it into simple
waves, saving the contribution of each wave to memory. Presently, BinPrism only works for periodic data (such as
daily or yearly patterns), but it is hoped that in the future more domains will be supported.

Website: https://github.com/JoeJimFlood/binprism
Installation Instructions: https://github.com/JoeJimFlood/binprism/blob/master/doc/installation.md
Descriptions of Classes and Methods: https://github.com/JoeJimFlood/binprism/blob/master/doc/datastructure.md
Examples: https://github.com/JoeJimFlood/binprism/blob/master/doc/examples.md
'''
from .version import *
from .core import *
from .util import *

def dinosaur():
    print(' _____\n/  o  \\\n>      \\\n\\____   \\\n     \\   \\\n      \\   \\____________\n      |                \\\n      |                \\\\\n      |     ______     |\\\\\n      |    /      \\    | \\|\n      |    |      |    |\n      |____|      |____|\n\n         DINOSAUR!\n')
