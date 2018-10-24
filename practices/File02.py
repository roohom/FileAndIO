#!/usr/bin/env python
# File  : File02.py
# Author: roohom
# Date  : 2018/10/19 0019

# coding = gbk

f = open("FILE02.txt", "w")
f.write("十点半我在宿舍敲代码")
f.seek(0, 2)
length = f.tell()
f.close()
print("这个File的长度是：", length)

f = open("FILE02.txt", "a+")
f.write("\n其实也还行")
f.seek(0, 2)
len = f.tell()
f.close()
print("现在这个File的长度又是：", len)
