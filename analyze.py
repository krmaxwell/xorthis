#!/usr/bin/python

import base64
import sys

from cryptokrm import *

with open(sys.argv[1],'rb') as f:
    message = f.read()

# assumes input is base64
ctext = base64.b64decode(message)

# user-defined keysize
# suggest using values from keysize.py if not known
k = int(sys.argv[2])

# now split cipher
btext = [0]*k

fullkey = ''

for i in xrange(0,k):
    btext[i] = ctext[i::k]
    for key in xrange(0,256):
        cleardata = ''
        for j in xrange(0,len(btext[i])):
            data = ord(btext[i][j]) ^ key
            if data in xrange(32,127) or data == 10 or data == 13:
                cleardata += chr(data)
            else:
                break
        # BROKEN do not use
        if len(cleardata) == len(btext[i]):
            fullkey += chr(key)

print fullkey
