#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2019/5/20/025 21:29
@desc: 功能函数，APP 的重命名和移动
'''


import shutil
import os

if __name__ == "__main__":
    filePath = r'E:\APKDataSet\compareResults\FSquaDRA\5\5_小米市场应用数据集'
    f = os.listdir(filePath)
    # fileName = r'E:\apk\wandoujia\77777.txt'
    # f = open(fileName, encoding='UTF-8-sig')
    # DHashVal1 = f.readlines()
    for val in  f:
        # val = val.strip('\n').split(':')[2]

        valre = val.replace(";", '')
        valre = valre.replace(" ", '')
        valre = valre.replace("&", '')
        inPath = r'E:\APKDataSet\compareResults\FSquaDRA\5\5_小米市场应用数据集' + '\\' + val
        outPath = r"E:\APKDataSet\xiaomi\5" + '\\' + valre
        try:
            shutil.move(inPath,outPath)
        except:
            print(val)