#!/bin/env python3

import sys
import os
import stat
from pathlib import Path

# TODO
# Move to a main function
# Add sanity checks to make sure single arg exists

def help():
    print('''
    Usage:
    dir.py takes only one argument.

    Example:
    ./dir.py /home/share/user/Documents/abc/foo.bar
    ''')
    sys.exit(1)

def getperms(filepath):
    st = os.stat(filepath)
    octals = oct(st.st_mode)
    return octals[-4:]

def getugid(filepath):
    x = Path(filepath)
    uid = x.owner()
    gid = x.group()
    retstr = uid + ":" + gid
    return retstr

if len(sys.argv) != 2:
    help()

x=sys.argv[1]
y=[]
i=''
for dir in x.split('/'):
    if dir == '':
        continue
    y.append('/' + dir)
    s=''.join(str(i) for i in y)
    ugorwx = getperms(s)
    owner = getugid(s)
    print(owner, ugorwx, s)
