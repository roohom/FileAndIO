#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : search_file04.py
# Author: roohom
# Date  : 2018/10/26 0026

"""
统计文件夹下所有的文件类型及其数量
    - 打开目标文件夹
    - 获取文件夹下所有的文件
    - 判断类型，如果是文件夹也要进行下一步操作
    - 统计文件的类型机器数量
"""
import os

target_dir = input("请输入所要查找的目标文件夹：")
os.chdir(target_dir)

all_files = os.listdir(os.curdir)                   # 获取当前目录下所有的文件

type_dic = {}

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dic.setdefault("文件夹", 0)
        type_dic["文件夹"] += 1
    else:
        ext = os.path.splitext(each_file)[1]             # 获取文件的后缀名
        type_dic.setdefault(ext, 0)
        type_dic[ext] += 1

for each_type in type_dic:
    print("该文件夹下有类型为{}的文件{}个".format(each_type, type_dic[each_type]))
