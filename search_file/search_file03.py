#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : search_file03.py
# Author: roohom
# Date  : 2018/10/23 0023

"""
搜索文件脚本 version 1.0
    - 用户输入文件目录和目标文件的名称，开始在目标文件夹里搜索目标文件，结果返回目标文件所在的1文件夹名称
    - search_file函数负责工作
        - os.listdir列出文件夹里所有的文件
        - os.path.isdir判断文件是否为文件夹
            - 是，调用search_file函数，继续在文件夹内搜索目标文件
            - 否，pass
    -

    update to version 2.0
    新增模糊匹配
        - 输入不完整文件名，可以搜索匹配所有符合的文件
            - 使用in来判断不完整的文件名是否包含在文件名中
    update to version 3.0
    新增将多搜索到的文件目录地址保存到指定的文本文件中
        - 文件的读写操作
"""

import os
start_dir = input("请输入起始目录名：")
target_file = input("请输入目标文件名：")

reserv = []

def search_file(start_dir, target_file):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        if target_file in each_file:                    # 模糊匹配，判断不完整的文件名是否包含在所搜索的文件名中
            file_name = os.getcwd() + os.sep + each_file
            reserv.append(file_name)
            print(file_name)
        if os.path.isdir(each_file):
            search_file(each_file, target_file)         # 递归调用，进入文件夹继续查找目标文件
            os.chdir(os.pardir)
    return reserv


rsp = search_file(start_dir, target_file)
print(rsp)
fp = open(os.getcwd() + os.sep + "reserv.txt", "wb")                           # 默认在程序所在的文件夹
fp.write("\n".join(rsp).encode("utf-8"))
fp.close()

