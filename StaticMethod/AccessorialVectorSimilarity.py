#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: AccessorialVectorSimilarity.py
@time: 2019/1/2/002 11:07
@desc: 辅助特征向量的相似性
'''
import os
import numpy
from decimal import Decimal

#从文件中读取并进行相似性的比较
def readTxtToArrayAndCompareSimilarity(fileName1,fileName2):
        if os.path.exists(fileName1):
            f = open(fileName1)
            vectorVal1 = f.readlines();
            f.close()
            vectorVal1 = vectorVal1[0].strip('\n')
            vectorArr_1 = strToArr(vectorVal1)
        else:
            print("There is no such file")
        if os.path.exists(fileName2):
            f = open(fileName2)
            vectorVal2 = f.readlines();
            f.close()
            vectorVal2 = vectorVal2[0].strip('\n')
            vectorArr_2 = strToArr(vectorVal2)
        else:
            print("There is no such file")

        simVal = str(cosSimilarity(vectorArr_1,vectorArr_2))
        return simVal


#字符串转换为数组 ------> '[1,2,3]'---> [1,2,3]
def strToArr(str):
    resArr = []
    strArr = str.split(',')
    for i in range(len(strArr)):
        if i == 0:
            strArr[i] = strArr[i].strip('[')
        if i == (len(strArr) - 1):
            strArr[i] = strArr[i].strip(']')
        resArr.append(float(strArr[i]))
    return resArr


#余弦相似度
def cosSimilarity(arr1, arr2):
    if len(arr1) != len(arr2):
        return 0
    denominator1 = 0
    denominator2 = 0
    numerator = 0
    for i in range(len(arr1)):
        numerator += arr1[i] * arr2[i]
        denominator1 += numpy.square(arr1[i])
        denominator2 += numpy.square(arr2[i])
    resSimNum = numerator / (numpy.sqrt(denominator1) * numpy.sqrt(denominator2))
    resSimNum = Decimal(resSimNum).quantize(Decimal('0.000'))
    resSimNum = float(resSimNum)
    return resSimNum
