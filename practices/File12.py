#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File12.py
# Author: roohom
# Date  : 2018/10/26 0026

"""
写文件脚本
    - 接收用户的输入，并将输入写入文件
"""

file_name = input("请输入文件名：")


def file_writer(file_name):
    f = open(file_name, "w")
    print("请输入你想写入的内容，以exit保存并退出。")

    while True:
        fp = input()

        if fp == "exit":
            break
        else:
            f.write("{}\n".format(fp))

    f.close()


file_writer(file_name)
