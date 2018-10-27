#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File14.py
# Author: roohom
# Date  : 2018/10/27 0027


"""
程序功能：
    - 接收用户的输入的的文件名和行数n，并将该文件的前n行内容打印
    - 如果输入的文件名称不是文件，则提示用户继续输入
"""
import os

file_name = None
file_line = None


def file_printer(file_name, file_line):
    while True:
        file_name = input("请输入你想打开的文件名：")
        file_line = input("请输入行数：")
        if os.path.isfile(file_name):
            print("文件{}的前{}行内容如下：".format(file_name, file_line))
            fp = open(file_name, "r")
            for i in range(int(file_line)):
                print(fp.readline().strip("\n"))
            break
        else:
            print("你输入的文件名不是一个文件！")
            print("是否选择重新输入？yes/no", end=" ")
            go = input()
            if go == "no":
                break
            elif go == "yes":
                continue
            else:
                break
    fp.close()


if __name__ == '__main__':
    file_printer(file_name, file_line)

