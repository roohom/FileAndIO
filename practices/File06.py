#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File06.py
# Author: roohom
# Date  : 2018/10/20 0020

'''
二进制文件的读取
    - strut模块pack()方法写的文件应该用read()方法读取
    - pickle模块的dump()方法写的文件应该使用pickle模块的load()方法还原对象
'''

# 使用struct模块的unpack()方法还原，读取File03.txt的文件内容

import struct
f = open("FILE03.dat", "rb")
sn = f.read(9)
tu = struct.unpack("if?", sn)
print(tu)
n = tu[0]
x = tu[1]
b1 = tu[2]
print(n)
print(x)
print(b1)
s = f.read(9)
f.close()
print(s)
print("="*30)

# 使用pickle模块的load()模块方法还原
import pickle

f = open("FILE04.dat", 'rb')
s = pickle.load(f)
i = 0
while i < s:
    m = pickle.load(f)
    print(m)
    i += 1
f.close()
