#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File03.py
# Author: roohom
# Date  : 2018/10/20 0020

# 二进制文件的写入

'''
二进制文件的写入有两种方法
    - struct模块的pack()方法把数字和布尔值转换为字节穿，然后用write()方法写进二进制文件中
        - pack(格式串，数字对象表)
    - pickle模块的dump()方法直接把俺对象转换为字节串（bytes）并存入文件中
        - dump(object, i)
'''

import struct

a = 1024000
b = 10.24
c = True
d = "我早上八点在图书馆写代码"
e = struct.pack("if?", a, b, c)
f = open("FILE03.dat", "wb")
f.write(e)
f.close()

