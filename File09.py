#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File09.py
# Author: roohom
# Date  : 2018/10/21 0021


# 将结构化数据写入文件并作相关的处理


import struct

f = open("FILE09.dat", "wb")
n = input("请输入学生人数：")
s = struct.pack("i", int(n))
f.write(s)

s2 = "学号 姓名 C语言从学习到转行 C++从入门到放弃 MySQL从删库到跑路"
f.write(bytes(s2, "UTF-8"))
i = 0

while i < int(n):
    num = input("请输入第" + str(i+1) + "人的学号（2位）：")
    name = input("请输入姓名：")
    a1 = input("请输入C语言从学习到转行成绩：")
    a2 = input("请输入从C++从入门到放弃成绩：")
    a3 = input("请输入MySQL从删库到跑路成绩：")

    s = num + name
    s1 = s + str(struct.pack("fff", int(a1), int(a2), int(a3)))

    f.write(bytes(s1, "utf-8"))
    i += 1
f.close()
