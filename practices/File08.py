#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File08.py
# Author: roohom
# Date  : 2018/10/20 0020

# 将FILE07.txt中的"Hi"替换为Hello

# 定义一个函数完成文件的复制

def File_Copy(tar_file, res_file):
    try:
        f1 = open(res_file, "rb")
        f2 = open(tar_file, "wb")
        s = f1.read()
        f2.write(s)

        f1.close()
        f2.close()
        return 0

    except:
        print("哎呀妈呀文件打开失败了！")
        return -1
    # global f1, f2


try:
    File_Copy("FILE0701.txt", "FILE07.txt")
    a = open("FILE0701.txt", "r")
    a2 = open('FILE0702.txt', "w+")
except:
    print("文件打开异常！")

while True:
    s = a.read(2)
    point = a.tell()
    if len(s) < 2:
        break
    if s == "Hi":
        a2.write('Hello')
    else:
        a2.write(s[0])
        a.seek(point - 1)