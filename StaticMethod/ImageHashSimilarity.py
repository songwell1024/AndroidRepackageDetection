#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: ImageHashSimilarity.py
@time: 2019/1/2/002 11:02
@desc: 图片文件哈希值的相似性
'''
import os
from StaticMethod.HungarianAlgorithm import HungarianAlgorithm
from decimal import Decimal


#比较图片资源哈希的值的汉明距离
def compareImgSimilarity(fileName1, fileName2):
    if os.path.exists(fileName1):
        f = open(fileName1)
        DHashVal1 = f.readlines();
        f.close()
    else:
        print("There is no such file")
    if os.path.exists(fileName2):
        f = open(fileName2)
        DHashVal2 = f.readlines();
        f.close()
    else:
        print("There is no such file")
    nx = []
    edge = {}
    cx = {}
    key_index = 0
    for hashVal1 in DHashVal1:
        hashVal1 = hashVal1.strip('\n')
        key_i = 0
        edge_y = {}
        for hashVal2 in DHashVal2:
            hashVal2 = hashVal2.strip('\n')
            dist = hamming_distance_with_hash(hashVal1,hashVal2)
            if dist <= 5:
                edge_y[key_i] = 1 # 1 表示可以匹配， 0 表示不能匹配
                key_i = key_i + 1
            else:
                edge_y[key_i] = 0
                key_i = key_i + 1

        edge[key_index] = edge_y
        cx[key_index] = -1
        nx.append(key_index)
        key_index = key_index + 1
    ny = []
    cy = {}
    visited = {}
    key_i = 0
    for hashVal2 in DHashVal2:
        cy[key_i] = -1
        visited[key_i] = 0
        ny.append(key_i)
        key_i = key_i + 1
    simRes = HungarianAlgorithm(nx, ny, edge, cx, cy, visited).max_match()
    simRes = simRes / min(DHashVal1.__len__(),DHashVal2.__len__())

    #四舍五入
    simRes = Decimal(simRes).quantize(Decimal('0.000'))
    simRes = float(simRes)

    return str(simRes)


#hash值之间的汉明距离
def hamming_distance_with_hash(dhash1, dhash2):
    difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
    return bin(difference).count("1")
