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

import StaticMethod.ImageHashSimilarity as IHS

import datetime


if __name__ == '__main__' :

    ApkFilePath = r'C:\Users\Song\Desktop\dataSEt'
    startTime = datetime.datetime.now()
    # CIH.SaveDHashValueToTxt(ApkFilePath)
    # PAM.getAccessorialVectorOfApp(ApkFilePath)
    ASS.readTxtToArrayAndCompareSimilarity(ApkFilePath)
    endTime = datetime.datetime.now()
    # print('执行时间： ' + str((endTime - startTime).microseconds / 10e6) + 's')