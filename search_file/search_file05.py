#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : search_file05.py
# Author: roohom
# Date  : 2018/10/26 0026

"""
计算一个文件下所有文件的大小
    - 打开文件夹
    - 遍历所有文件
    - 获取文件大小并打印
"""


import os

target_folder = input("请输入你想进入的文件夹：")
os.chdir(target_folder)
all_file = os.listdir(target_folder)
file_info = {}

for each_file in all_file:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_info[each_file] = file_size

for file in file_info.items():
    if file[1] > 1024:
        print("{}文件的大小为：{}KB".format(file[0], int(file[1])/1024))
    else:
        print("{}文件的大小为：{}字节".format(file[0], int(file[1])))

