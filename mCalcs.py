from calcs import plus, minus, mul, div
print(plus(3,5))

import calcs
print(calcs.plus(3,5))

import sys, os
print('path >>',sys.path)
print('cwd >>',os.getcwd())
os.chdir('..')
print('cwd >>',os.getcwd())