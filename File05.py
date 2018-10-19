#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File05.py
# Author: roohom
# Date  : 2018/10/20 0020

'''
文本文件的读取
    - read[size], 文件大于size字节，只读取size字节，若文件小于size字节，则读取完。如不设置size，则读取全部。
    - readline([size])，读取一行。
    - readlines([seze])，读取完文件
'''

f = open("FILE01.txt", "r")                  # 此处读取的是GBK编码的中文字符
s = f.read(11)
f.close()
print("s=", s)
print("字符串s的长度：", len(s))
print("="*30)
# 读取FILE01.txt的全部字符

f = open("FILE01.txt", "r")
s= f.read()
f.close()
print(s)
print(len(s))
print("="*30)

# 使用readline()读取FILE02.txt的每一行

file = open("FILE02.txt", "r")

while True:
    s = file.readline()
    print(s)
    if s == "":
        break

print("="*30)

# 使用readlines()读取FILE02.txt每一行

FILE = open("FILE02.txt", "r")
m = FILE.readlines()
for i in m:
    print(i)
    FILE.close()
