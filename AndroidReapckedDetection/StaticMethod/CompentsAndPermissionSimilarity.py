#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: AccessorialVectorSimilarity.py
@time: 2019/1/2/002 11:07
@desc: 组件和权限比较相似性
'''

import StaticMethod.CompentsAndPermission as CAP
import os
from decimal import Decimal

#组件和权限比较相似性
def compareSimilarityByComponentsAndPermission(fileName1, fileName2):
    identical = 0;
    similar = 0;
    new = 0;
    deleted = 0;
    dict1 = {}
    dict2 = {}
    similarity = "none"

    if os.path.exists(fileName1):
       dict1 = CAP.getElementFrequency(fileName1)
    else:
        print("There is no such file--" + fileName1)
    if os.path.exists(fileName2):
        dict2 = CAP.getElementFrequency(fileName2)
    else:
        print("There is no such file--" + fileName2)
    if dict1.__len__() > 0 and dict2.__len__() > 0:
        for key in dict1.keys():
            if dict2.__contains__(key) and dict2[key] == dict1[key]:
                identical = identical + 1;
                del dict2[key]
            elif dict2.__contains__(key) and dict2[key] != dict1[key]:
                similar = similar + 1
                del dict2[key]
            elif not dict2.__contains__(key):
                deleted = deleted + 1;

        new = dict2.__len__()

        total = identical + similar + new + deleted
        similarity = max(identical / (total - new), identical / (total - deleted))

        # 四舍五入
        similarity = str(float(Decimal(similarity).quantize(Decimal('0.000'))))

    return similarity
