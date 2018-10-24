#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File11.py
# Author: roohom
# Date  : 2018/10/22 0022


import struct


with open("FILE09.dat", "rb") as fp:
    s = fp.read(4)                                 # 读出人数
    n, = struct.unpack("i", s)
    print("n=", n)
    print()
    m = fp.read(15+48+10+12)                                 # 读出表头 一个汉字3个字节 一个空格1个字节 一个英文字符1个字节
    print(m.decode("utf-8"))
    for i in range(n):
        l = fp.read(2)                                           # 读出学号
        print(l.decode("utf-8")+" "*1, end="")
        m = fp.read(3*3)                                         # 读出姓名
        print(m.decode("utf-8") + " "*7, end="")
        for j in range(3):
            m = fp.read(2)                                           # 读出成绩
            print(m.decode("utf-8") + " "*12,end="")
        print()


