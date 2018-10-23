#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File0301.py
# Author: roohom
# Date  : 2018/10/22 0022

import struct

f = open("FILE03.dat", "rb")
sn = f.read(10)
c, d= struct.unpack('if', sn)
print(c, d)


s = f.read(9)
f.close()
print(s)
