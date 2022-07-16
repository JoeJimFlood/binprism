from setuptools import setup, find_packages

setup(
    name = 'binprism',
    version = '1.1',
    description = 'Package for fitting continuous profiles to binned data',
    url = 'https://github.com/JoeJimFlood/BinPrism',
    author = 'Joseph J. Flood',
    author_email = 'joejimflood@gmail.com.com',
    license = 'GNU GPLv3',
    keywords = 'data_analysis simulation',
    packages = find_packages('binprism'),
    install_requires = [
          'numpy',
          'pandas',
          'scipy',
          'matplotlib'
      ],

)
