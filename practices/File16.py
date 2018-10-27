#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : File16.py
# Author: roohom
# Date  : 2018/10/27 0027

"""
程序功能：
    - 替换文件制定的字符串为新的字符串
    - rep_word
    - new_word
"""
file_name = input("请输入你要打开的文件名：")
rep_word = input("请输入你要替换的字符串：")
new_word = input("请输入你要替换成的新字符串：")


def rep_word_func(file_name, rep_word, new_word):
    f = open(file_name)
    content = []

    for eachline in f:
        if rep_word in eachline:
            eachline = eachline.replace(rep_word, new_word)
        content.append(eachline)

    decide = input("确定要这么做吗？yes/no")
    if decide in ["YES", "Yes", "yes"]:
        f_write = open(file_name, "w")
        f_write.write("".join(content))
        f_write.close()

if __name__ == '__main__':
    rep_word_func(file_name, rep_word, new_word)