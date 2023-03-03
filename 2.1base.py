#!/usr/bin/python3

import sys
print('Python路徑argv:')
for i in sys.argv:
    print(i)
print('Python路徑import:\n', sys.path)

from sys import argv, path
print('Python路徑from:\n', path)
