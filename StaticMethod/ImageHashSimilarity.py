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


#比较图片资源哈希的值的汉明距离
def compareImgSimilarity(fileName1, fileName2):
    SimRes = 0
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
    for hashVal1 in DHashVal1:
        dist = 32
        hashVal1.strip('\n')
        for hashVal2 in DHashVal2:
            hashVal2.strip('\n')
            dist = min(hamming_distance_with_hash(hashVal1,hashVal2), dist)
            if dist == 0:
                break
        if dist <= 5:
            SimRes = SimRes + 1;
    SimRes = SimRes / DHashVal1.__len__()
    return str(SimRes)


#hash值之间的汉明距离
def hamming_distance_with_hash(dhash1, dhash2):
    difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
    return bin(difference).count("1")
