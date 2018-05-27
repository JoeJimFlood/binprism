import sys
import os
from shutil import copytree

current_dir = os.path.split(__file__)[0]

if len(sys.argv) == 1:
    if sys.version[0] == '2':
        from Tkinter import Tk
        Tk().withdraw()
        from tkFileDialog import askdirectory
    elif sys.version[0] == '3':

        from tkinter.filedialog import askdirectory
    else:
        raise EnvironmentError('Invalid Python version')
    target_dir = askdirectory(title = 'Select Python Directory')

else:
    target_dir = os.path.join(sys.argv[1], 'Lib', 'site-packages', 'binprism')

if os.path.exists(target_dir):
    print('BinPrism already installed')

else:
    copytree(os.path.join(current_dir, 'binprism'), target_dir)
    print('BinPrism installed!')