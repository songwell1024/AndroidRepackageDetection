#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: ACS.py
@time: 2018/12/24/024 15:31
@desc:
所有公共子序列
'''
import math
from decimal import Decimal

def getSimilarityByAcs(s,t):
    m = s.__len__()
    n = t.__len__()
    res = [[0] * (n ) for i in range(m)]
    help_index = 0
    for i in range(0, m ):
        for j in range(0, n):
            help_index = getNumberOfCommonDistinctSubsequences(s[i], t[j]) / \
                        (math.sqrt(getNumberOfCommonDistinctSubsequences(s[i], s[i]) * getNumberOfCommonDistinctSubsequences(t[j], t[j])))
            help_index = Decimal(help_index).quantize(Decimal('0.00'))
            res[i][j] = float(help_index)
    return res

def getNumberOfCommonDistinctSubsequences(arr_s, arr_t):
    # arr_s = s_str.split()
    # arr_t = t_str.split()
    m = arr_s.__len__()
    n = arr_t.__len__()
    #初始化
    numSequence = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(0, m+1 ):
        numSequence[i][0] = 1
    for j in range(0, n+1 ):
        numSequence[0][j] = 1
    numSequence[0][0] = 0;
    #计算矩阵的过程
    for i in range(1,m +1):
        for j in range(1, n+1):
            if L(arr_t,arr_s[i-1],j-1) == 0:
                numSequence[i][j] = numSequence[i-1][j]
            elif L(arr_t,arr_s[i-1],j-1) > 0 and L(arr_s,arr_s[i-1],i-1-1) == 0:
                numSequence[i][j] = numSequence[i - 1][j] + numSequence[i - 1][L(arr_t,arr_s[i-1],j-1)]
            elif L(arr_t,arr_s[i-1],j-1) > 0 and L(arr_s,arr_s[i-1],i-1-1) > 0:
                numSequence[i][j] = numSequence[i - 1][j] + numSequence[i - 1][L(arr_t, arr_s[i-1], j-1)] - numSequence[L(arr_s,arr_s[i-1],i-1-1) - 1][L(arr_t,arr_s[i-1],j-1)]
    return numSequence[m][n]

def L(str_array, letter, index):
    if index < 0:
        return 0
    maxRes = 0;
    for i in range(0,index + 1):
        if str_array[i] == letter:
            maxRes = i;
    return maxRes;



# 所有公共子序列
# def getNumofCommonSubstr(str1, str2):
#     lstr1 = len(str1)
#     lstr2 = len(str2)
#     record = [[0 for i in range(lstr2 + 1)] for j in range(lstr1 + 1)]  # 多一位
#     maxNum = 0  # 最长匹配长度
#     max_end = 0  # 匹配的终止
#     max_start=0 #匹配的起始位
#     map_maxStr={}#key为开始位置，value为最大匹配字符串
#     for i in range(lstr1):
#         for j in range(lstr2):
#             if str1[i] == str2[j]:
#                 # 相同则累加
#                 record[i + 1][j + 1] = record[i][j] + 1
#                 if record[i + 1][j + 1] > maxNum:
#
#                     # 获取最大匹配长度
#                     maxNum = record[i + 1][j + 1]
#                     # 记录最大匹配长度的开始位置
#
#                     p= i + 1
#                     max_start=i+1 - maxNum
#                     map_maxStr[max_start]=str1[p - maxNum:p]
#                     maxNum=0
#     # return str1[p - maxNum:p], maxNum
#     return map_maxStr


# map_maxStr = {}
# map_maxStr = ACS.getNumofCommonSubstr(s1, s2)  # 返回匹配字符串
# for m in map_maxStr:
#     print(map_maxStr.get(m))
#
# map_maxStr = ACS.getNumofCommonSubstr(s22, s11)  # 返回匹配字符串
# for m in map_maxStr:
#     print(map_maxStr.get(m))



