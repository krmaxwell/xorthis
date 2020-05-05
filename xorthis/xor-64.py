#!/usr/bin/env python3

import sys
import base64

from .cryptokrm import xorstr

with open(sys.argv[1], 'rb') as f:
    s = f.read()

print(xorstr(base64.b64decode(s), sys.argv[2]))
