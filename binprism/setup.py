from setuptools import setup, find_packages

setup(
    name='binprism',
    version='1.1',
    license='GNU GPLv3',
    author='Joseph J. Flood',
    author_email='joejimflood@gmail.com.com',
    packages=find_packages('binprism'),
    package_dir={'': 'binprism'},
    url='https://github.com/JoeJimFlood/BinPrism',
    keywords='binprism',
    install_requires=[
          'numpy',
          'pandas',
          'scipy',
          'matplotlib'
      ],

)
