#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File13.py
# Author: roohom
# Date  : 2018/10/26 0026

"""
比较文件不同
    - 使用readline逐行读文件
    - 将所读出来的两个文件的每行内容进行比对
    - 对不同内容的一行，提示不同，并打印行数和不同之处
    局限
        - 只能根据file1文件的行数来比较不同，如果file2的行数大于file1的行数，file2多出的行将相当于没有
"""
file1 = input("请输入需要比对的第一个文件：")
file2 = input("请输入需要比对的第二个文件：")


def file_compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)

    line = 0                           # mark
    diff = {}                          # container

    for line1 in f1:                   # 局限之处，只能根据file1的行数进行比较不同
        line2 = f2.readline()

        line += 1
        if line1 != line2:
            print("第{}行的内容不同".format(line))
            diff["第{}行".format(line)] = "{} -- {}".format(line1, line2)
    print(diff)
    while True:
        if len(diff) == 0:
            print("所比较的两个文件完全相同！")
        else:
            print("两个文件有{}处不同,具体为：".format(len(diff)))
            for j, k in diff.items():
                print(j, k)
        if line > len(diff):
            break
    f1.close()
    f2.close()


if __name__ == '__main__':
    file_compare(file1, file2)
