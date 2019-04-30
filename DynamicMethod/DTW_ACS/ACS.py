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
    res = [[0] * (n) for i in range(m)]
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
    numSequence[0][0] = 0
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
    maxRes = 0
    for i in range(0,index + 1):
        if str_array[i] ==  letter:    # 在这里做了元素的比较 也就值字符串的比较
            maxRes = i
    return maxRes


##比较树中一个元素是否相等，布局结构 + 布局属性
def ElementEqual(element1, element2):
    ele1 = element1.split(':')
    ele2 = element2.split(':')
    index = 0
    if ele1[0] == ele2[0]:
        for i in range(1, ele1.__len__()):
          if ele1[i] == ele2[i]:
              index = index + 1
    if index > ((ele1.__len__() -1) * 0.5):
        return True
    else:
        return False