#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/12/25/025 21:29
@desc:
'''

import StaticMethod.ProcessAndroidManifest as PAM
import StaticMethod.CalculateImageHash as CIH
import StaticMethod.AppStaticSimlarity as ASS
import StaticMethod.DataProcessAndShow as DPAS

import datetime




if __name__ == '__main__' :

    # ApkFilePath = r'C:\Users\Song\Desktop\test'  # 数据集文件
    # # OutPutSimFile = r'C:\Users\Song\Desktop\AppSimTxt\AppSimValue.txt'  # APP的相似性文件
    # startTime = datetime.datetime.now()
    # CIH.SaveDHashValueToTxt(ApkFilePath)   #计算感知哈希
    # PAM.getAccessorialVectorOfApp(ApkFilePath)  # 计算权限组件个数的向量
    # # ASS.readTxtToArrayAndCompareSimilarity(ApkFilePath, OutPutSimFile)  #相似性比较
    # ASS.readTxtToArrayAndCompareSimilarity(ApkFilePath)  #相似性比较
    # endTime = datetime.datetime.now()
    # print('执行时间： ' + str((endTime - startTime)) + 's')
    fileName1 = r'C:\Users\Song\Desktop\dataSEt\AppSimValue.txt'
    fileName2 = r'C:\Users\Song\Desktop\val\3.txt'
    DPAS.dataPeocessAndShow(fileName2)
