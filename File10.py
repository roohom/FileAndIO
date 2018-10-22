#!/usr/bin/env python
# -*- coding: gbk -*-
# File  : File10.py
# Author: roohom
# Date  : 2018/10/21 0021

import struct

f = open("FILE09.dat", "rb")
s = f.read(4)                                         # 读出人数所占的4个字节
n, = struct.unpack("i", s)
print("n=", n)
head = f.read(40*2)
i = 0
li = []
while i < n+1:
    i += 1
    s = f.read(11)                                # 读出学号
    num = s
    s = f.read(3*2)
    name = s
    s = f.read(4*3)
    a1, a2, a3 = struct.unpack("fff", s)
    a4 = (a1+a2+a3)/3
    li2 = [num, name, a1, a2, a3, a4]
    li.append(li2)


i = 0
j = 0

#print(struct.unpack("s", head)[0] + "平均分")
while i < n:
    s2 = (li[i][0]+bytes("", "gbk"))
    s2 = s2 + li[i][1] + bytes("", "gbk")*4
    j = 2
    while j < 6:
        s = "%-13.2f" % li[i][j]
        j = j+1
        s2 = s2 + bytes(s, "gbk")
        print(s2)
        i = i + 1

