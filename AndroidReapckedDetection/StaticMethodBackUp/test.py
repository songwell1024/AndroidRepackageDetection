#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: test.py
@time: 2019/1/4/004 14:30
@desc:
'''
import numpy
from decimal import Decimal

#余弦相似度
def cosSimilarity(arr1, arr2):
    if len(arr1) != len(arr2):
        return 0
    denominator1 = 0
    denominator2 = 0
    numerator = 0
    for j in range(len(arr1)):
        arr1[j] = float(arr1[j])
        arr2[j] = float(arr2[j])
        numerator += arr1[j] * arr2[j]
        denominator1 += numpy.square(arr1[j])
        denominator2 += numpy.square(arr2[j])
    resSimNum = numerator / (numpy.sqrt(denominator1) * numpy.sqrt(denominator2))
    resSimNum = Decimal(resSimNum).quantize(Decimal('0.00'))
    resSimNum = float(resSimNum)
    return resSimNum

def EuclideanDistance(arr1, arr2):
    if len(arr1) != len(arr2):
        return 0
    sum = 0
    for i in range(len(arr1)):
        arr1[i] = float(arr1[i])
        arr2[i] = float(arr2[i])
        sum = sum + numpy.square((arr1[i] - arr2[i]))

    dist = numpy.sqrt(sum);
    EDSim = 1 / (1 + dist)
    EDSim =  dist
    EDSim = Decimal(EDSim).quantize(Decimal('0.00'))
    EDSim = float(EDSim)
    return EDSim

import StaticMethod.AccessorialVectorSimilarity as AIS

if __name__ == '__main__':
    # arr1 = [95, 9, 609, 35, 8, 76]
    # arr2 = [200, 3, 302, 16, 8, 25]
    # arr3 = [83, 3, 306, 16, 8, 26]
    # arr4 = [58, 3, 217, 22, 5, 35]
    arr1 = [95, 9, 609, 35, 8, 76, 13648, 268, 56, 69945]
    arr2 = [200, 3, 302, 16, 8, 25, 1843, 124, 12, 2000]
    # print(EuclideanDistance(arr1,arr2))
    print(cosSimilarity(arr1, arr2))
    # print(cosSimilarity(arr1, arr3))
    # print(cosSimilarity(arr1, arr4))
    # print(cosSimilarity(arr2, arr3))
    # print(cosSimilarity(arr2, arr4))
    # print(cosSimilarity(arr3, arr4))
    # fileName1 = r'C:\Users\Administrator\Desktop\AppXml\dataSEt\1\com.wifi.key.fromXiaomi\AccessorialVector.txt'
    #
    # fileName2 = r'C:\Users\Administrator\Desktop\AppXml\dataSEt\1\com.tencent.mobileqq.fromXiaomi\AccessorialVector.txt'
    # print(AIS.readTxtToArrayAndCompareSimilarity(fileName1,fileName2))