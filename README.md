# BinPrism
Tools for fitting linear combinations of continuous basis functions to match binned data.

Often, data from continuous variables are placed into discrete bins.
BinPrism fits continuous profiles to match these bins, allowing for the ability to produce clean visualizations, re-aggregate data into differently-sized bins, and simulate random values folling a continuous distribution matching the original data. Like a prism separating light into different colors, BinPrism takes in binned data and separates it into simple waves, saving the contribution of each wave to memory. Presently, BinPrism only works for periodic data (such as daily or yearly patterns), but it is hoped that in the future more domains will be supported.
![Demonstration of BinPrism](doc/BinPrismDemo.gif)

## Contents
[Installation](doc/installation.md) <br />
[Data Structure](doc/datastructure.md) <br />
[Methodology](doc/methodology.md) <br />
[Examples](doc/examples.md) <br />
