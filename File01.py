#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File01.py
# Author: roohom
# Date  : 2018/10/19 0019

# 文件的写入


import codecs

s = "九点多我在图书馆敲代码"
f = codecs.open("FILE01.txt", "w", "utf-8")
f.write(s)
f.seek(0, 2)
length = f.tell()
f.close()
print("文件长度：", length)


f = codecs.open("FILE01.txt", "r+", "utf-8")
f.seek(0, 2)
f.write("其实也还行")
f.seek(0, 2)
len = f.tell()
f.close()
print("本次文件长度：", len)


