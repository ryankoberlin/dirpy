#!/bin/env python3

import sys
import os
import stat
from pathlib import Path

if len(sys.argv) == 1:
   print('provide a path as an argument ya knob')
   sys.exit()

x=sys.argv[1]
y=[]
i=''

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

for dir in x.split('/'):
    if dir == '':
        continue
    y.append('/' + dir)
    s=''.join(str(i) for i in y)
    ugorwx = getperms(s)
    owner = getugid(s)
    print(owner, ugorwx, s)
