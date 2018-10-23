#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Search_file.py
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
"""


import os

start_dir = input("请输入起始目录名：")
target_file = input("请输入目标文件名：")


def search_file(start_dir, target_file):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        if each_file == target_file:
            print(os.getcwd() + os.sep + each_file)
        if os.path.isdir(each_file):
            search_file(each_file, target_file)         # 递归调用，进入文件夹继续查找目标文件
            os.chdir(os.pardir)


search_file(start_dir, target_file)
