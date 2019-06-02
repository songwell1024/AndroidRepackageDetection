#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/12/25/025 21:29
@desc: 功能函数，用于统计APP的大小
'''

import os

def getAppSize(filePath):
    file_path_lists = os.listdir(filePath)
    i_0_10 = 0  #<10M
    i_10_20 = 0  #10 -20M
    i_20_30 = 0  # 20 -30M
    i_30_40 = 0  # 30 -40M
    i_40_50 = 0  # 40 -50M
    i_50_60 = 0  # 50 -60M
    i_60_70 = 0  # 60 -70M
    i_70_80 = 0  # 70 -80M
    i_80_90 = 0  # 80 -90M
    i_90_100 = 0  # 90 -100M
    i_100_200 = 0  # 100 -200M
    i_200_300 = 0  # 200 -300M
    i_300_400 = 0  # 300 -400M
    i_400_500 = 0  # 400 -500M
    i_500_1024 = 0  # 500 -1g
    i_1024 = 0  # >1g

    M = 1024 *1024

    for fileName in file_path_lists:
        fileName = filePath + '\\' + fileName
        size = os.path.getsize(fileName)
        if size <= M *10:
            i_0_10 = i_0_10 + 1
        elif size > 10*M and size <= 20*M:
            i_10_20 = i_10_20 + 1
        elif size > 20*M and size <= 30*M:
            i_20_30 = i_20_30 + 1
        elif size > 30*M and size <= 40*M:
            i_30_40 = i_30_40 + 1
        elif size > 40*M and size <= 50*M:
            i_40_50 = i_40_50 + 1
        elif size > 50*M and size <= 60*M:
            i_50_60 = i_50_60 + 1
        elif size > 60*M and size <= 70*M:
            i_60_70 = i_60_70 + 1
        elif size > 70*M and size <= 80*M:
            i_70_80 = i_70_80 + 1
        elif size > 80*M and size <= 90*M:
            i_80_90 = i_80_90 + 1
        elif size > 90*M and size <= 100*M:
            i_90_100 = i_90_100 + 1
        elif size > 100*M and size <= 200*M:
            i_100_200 = i_100_200 + 1
        elif size > 200*M and size <= 300*M:
            i_200_300 = i_200_300 + 1
        elif size > 300*M and size <= 400*M:
            i_300_400 = i_300_400 + 1
        elif size > 400*M and size <= 500*M:
            i_400_500 = i_400_500 + 1
        elif size > 500*M and size <= 1024*M:
            i_500_1024 = i_500_1024 + 1
        else:
            i_1024 = i_1024 + 1

    print(str(i_0_10) +"         <10M")
    print(str(i_10_20) +"        10 -20M")
    print(str(i_20_30) + "       20 -30M")
    print(str(i_30_40) + "       30 -40M")
    print(str(i_40_50) +"        40 -50M")
    print(str(i_50_60) + "       50 -60M")
    print(str(i_60_70) +"        60 -70M")
    print(str(i_70_80) +"        70 -80M")
    print(str(i_80_90) +"        80 -90M")
    print(str(i_90_100) +"       90 -100M")
    print(str(i_100_200) + "         100 -200M")
    print(str(i_200_300) + "         200 -300M")
    print(str(i_300_400) + "         300 -400M")
    print(str(i_400_500) + "         400 -500M")
    print(str(i_500_1024) + "        500 -1g")
    print(str(i_1024) + "        >1g")



if __name__ == '__main__':
    filePath = r'E:\apk\xiaomi\18'    # APP的路径
    getAppSize(filePath)