#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File07.py
# Author: roohom
# Date  : 2018/10/20 0020

# 统计文件中各种字符出现的次数

f = open("FILE07.txt", "w")
s = "Hi AaBbHi CCDscdjbjbweh0091jh8u81@Hi inehc A>a Hi apple!=banana"
f .write(s)
f.close()
f = open("FILE07.txt", "r")
nU = 0
nL = 0
n0 = 0
nR = 0
while True:
    x = f.read(1)
    if x == "":
        break
    elif x.islower():
        nL += 1
    elif x.isupper():
        nU += 1
    elif x.isdigit():
        n0 += 1
    else:
        nR += 1

f.close()
print(nU, nL, n0,  nR)

