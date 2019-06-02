#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2019/5/20/025 21:29
@desc: 功能函数，用于统计APP的大小
'''


import shutil

if __name__ == "__main__":
    fileName = r'E:\wandoujia\88888.txt'
    f = open(fileName)
    DHashVal1 = f.readlines()
    for val in  DHashVal1:
        val = val.strip('\n').split(':')[1]
        inPath = ""
        outPath = ""
        shutil.move(inPath,outPath)