#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File10.py
# Author: roohom
# Date  : 2018/10/21 0021

import struct
import time
import codecs

f = open("FILE09.dat", "rb")
s = f.read(4)                                         # 读出人数所占的4个字节
n, = struct.unpack("i", s)
print("n=", n)
for p in range(12, 100):
    head = f.read(p)                                  # 读出标题
    i = 0
    li = []
    print(f.tell())

    while i < n+1:
        i += 1
        s = f.read(4)                                # 读出学号
        num = s
        s = f.read(3*2)                              # 读出姓名
        name = s
        s = f.read(4*3)                              # 读出三门成绩
        a1, a2, a3 = struct.unpack("iii", s)
        a4 = (a1+a2+a3)/3
        li2 = [num, name, a1, a2, a3, a4]
        li.append(li2)
    i = 0
    j = 0

    # print(struct.unpack("s", head)[0] + "平均分")
    while i < n:
        s2 = (li[i][0])
        s2 = s2 + li[i][1]
        j = 2
        while j < 6:
            s = "{}".format(li[i][j])
            j = j+1
            s2 = s2 + s.encode("utf-8")
            print(s2.decode("utf-8"))
            i = i + 1
    time.sleep(0.5)
    f.seek(0)

# print(len("学号 姓名 C语言从学习到转行 C++从入门到放弃 MySQL从删库到跑路"))
