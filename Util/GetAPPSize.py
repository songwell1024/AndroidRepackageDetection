#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/5/05/025 21:29
@desc: 功能函数，用于统计APP的大小
'''

import os

def getAppSize(filePath):
    file_path_lists = os.listdir(filePath)
    i_20480 = 0  #小于20M
    i_20480_51200 = 0 #20 -50
    i_51200_102400 = 0  # 50 -100
    i_102400_153600 = 0  # 100 -150
    i_153600_204800 = 0  # 150 -200
    i_204800_307200 = 0  # 200 -300
    i_307200_409600 = 0  # 300 -400
    i_409600_512000 = 0  # 400 -500
    i_512000_1024000 = 0  # 500 -1000
    i_1024000_0 = 0  # >1000

    for fileName in file_path_lists:
        size = os.path.getsize(fileName)
        if size <= 20480:
            i_20480 = i_20480 + 1
        elif size > 20480 and size <= 51200:
            i_20480_51200 = i_20480_51200 + 1
        elif size > 51200 and size <= 102400:
            i_51200_102400 = i_51200_102400 + 1
        elif size > 102400 and size <= 153600:
            i_102400_153600 = i_102400_153600 + 1
        elif size > 153600 and size <= 204800:
            i_153600_204800 = i_153600_204800 + 1
        elif size > 204800 and size <= 307200:
            i_204800_307200 = i_204800_307200 + 1
        elif size > 51200 and size <= 102400:
            i_307200_409600 = i_307200_409600 + 1
        elif size > 409600 and size <= 512000:
            i_409600_512000 = i_409600_512000 + 1
        elif size > 512000 and size <= 1024000:
            i_512000_1024000 = i_512000_1024000 + 1
        else:
            i_1024000_0 = i_1024000_0 + 1
    print(i_20480,i_20480_51200,i_51200_102400,i_102400_153600,i_153600_204800
          ,i_204800_307200,i_307200_409600 ,i_409600_512000 ,i_512000_1024000,i_1024000_0)


if __name__ == '__main__':
    filePath = r'aa'    # APP的路径
    getAppSize(filePath)