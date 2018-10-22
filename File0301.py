#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File0301.py
# Author: roohom
# Date  : 2018/10/22 0022

import struct

f = open("FILE03.dat", "rb")
sn = f.read()
a, b, c, d, = struct.unpack('5s6sif', sn)
print(a, b, c, d)


s = f.read(9)
f.close()
print(s)
