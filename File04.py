#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File04.py
# Author: roohom
# Date  : 2018/10/20 0020

import pickle

f = open("FILE04.dat", "wb")
a = 7
b = 1020000
c = 10.24
d = "九点钟我在图书馆的窗边写代码"
li = [[1,2,3], [4,5,6], [9,8,7]]
tu = ("apple", "lenovo", "xiaomi")
set = {1,2,5,6}
dict = {"a":"apple", "l":"lenovo", "x":"xiaomi"}

try:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)
    pickle.dump(d, f)
    pickle.dump(li, f)
    pickle.dump(tu, f)
    pickle.dump(set, f)
    pickle.dump(dict, f)
except:
    print("文件写入异常！")
f.close()

