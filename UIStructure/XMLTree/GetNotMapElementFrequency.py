#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: GetNotMapElementFrequency.py
@time: 2018/11/16/016 15:11
@desc:  获取未被映射成字母的自定义UI元素和安卓自带元素的出现的频率
'''

import os
import glob

# 得到没有进行映射的元素出现的频率
def remainingElementFrequency(filePath):
    filePathList = os.listdir(filePath);
    for i in filePathList:
        fileList = os.path.join(filePath,i);
        fileList = glob.glob(os.path.join(fileList, '*'))
        for file in fileList:
            ApkName = os.path.splitext(file)[0]  # 将txt文件按照它们的文件名和后缀做一个分割
            ApkName = ApkName.split('\\')[-1]
            f = open(file)
            contents = f.readlines()
            length = 0;
            ele_per = 0;
            ele_and = 0;
            for msg in contents:
                msg = msg.strip('\n')
                length =  length + len(msg)
                ele_and = ele_and + msg.count('&')
                ele_per = ele_per + msg.count('%')
            print(ApkName + ": The frequency of '%' is ",ele_per/length)
            print(ApkName + ": The frequency of '&' is ",ele_and/length)





