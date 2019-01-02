#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: dtwAcs.py
@time: 2018/12/25/025 9:57
@desc:
'''
import math
from decimal import Decimal
import numpy

def DTW_ACS(arr_acs):
    m = arr_acs.__len__()
    n = arr_acs[0].__len__()
    dtw_acs = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m+1):
        dtw_acs[i][0] = float('inf')   #无穷大
    for j in range(n+1):
        dtw_acs[0][j] = float('inf')
    dtw_acs[0][0] = 0

    theta = [[0] * (n) for i in range(m)]

    for i in range(m):
        for j in range(n):
            theta[i][j] = 1 - arr_acs[i][j]

    for i in range(1,m+1):
        for j in  range(1, n+1):
            help_index = min(dtw_acs[i][j-1], dtw_acs[i-1][j], dtw_acs[i-1][j-1]) + theta[i-1][j-1]
            dtw_acs[i][j] = float(Decimal(help_index).quantize(Decimal('0.00')))
    # # return dtw_acs[m][n]

    for i in range(m+1):
        dtw_acs[i][0] = 0   #无穷大
    for j in range(n+1):
        dtw_acs[0][j] = 0

    # return dtw_acs
    return dtw_acs[m][n]/numpy.max(dtw_acs)
