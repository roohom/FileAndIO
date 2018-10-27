#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File15.py
# Author: roohom
# Date  : 2018/10/27 0027

"""
在File15.py的基础上新增：
    - 可以将用户任意输入的行数打印显示，如打印第3行到第5行的内容

    输入示例：
        - [2:5]表示2到5行
        - [:]表示全部行
        - [:5]表示第1行到第5行
"""
import os

file_name = None
file_line = None


def file_printer(file_name, file_line):
    while True:
        file_name = input("请输入你想打开的文件名：")
        file_line = input("请输入行数，示例为2:5：")
        if os.path.isfile(file_name):
            fp = open(file_name, "r")
            if ":" in file_line:
                print("文件{}的{}行内容如下：".format(file_name, file_line))
                begin, end = file_line.split(":")
                if begin == "":
                    begin = "1"
                if end == "":
                    end = "-1"
            else:
                print("文件{}的前{}行内容如下：".format(file_name, file_line))
                begin = 0
                end = int(file_line)

            begin = int(begin) - 1
            end = int(end)
            lines = end - begin
            for i in range(begin):
                fp.readline().strip("\n")
            if lines < 0:
                print(fp.read())
            else:
                for j in range(lines):
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
