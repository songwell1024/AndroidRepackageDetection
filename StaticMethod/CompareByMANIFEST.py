#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: ImageHashSimilarity.py
@time: 2019/1/2/002 11:02
@desc: 图片文件哈希值的相似性,不计算感知哈希，直接从MANIFEST下提取
'''
import os
from StaticMethod.HungarianAlgorithm import HungarianAlgorithm
from decimal import Decimal


#比较图片资源哈希的值的汉明距离
def compareImgSimilarityFromMANIFEST(fileName1, fileName2):
    HashVal1 = []
    HashVal2 = []
    if os.path.exists(fileName1):
        f = open(fileName1)
        H1 = f.readlines()
        f.close()
    else:
        H1 = []
        print("There is no such file--" + fileName1)  #看下出问题的文件夹
    if os.path.exists(fileName2):
        f = open(fileName2)
        H2 = f.readlines()
        f.close()
    else:
        H2 = []
        print("There is no such file--" + fileName2)

    for i in range(0, H1.__len__()):
        if H1[i].strip('\n').endswith('.png') or  H1[i].strip('\n').endswith('.jpg'):
            try:
                HashVal1.append(H1[i + 1].strip('\n').split(':')[1])
            except:
                print("error in compareImgSimilarityFromMANIFEST" + fileName1)

    for i in range(0, H2.__len__()):
        if H2[i].strip('\n').endswith('.png') or H2[i].strip('\n').endswith('.jpg'):
            try:
                HashVal2.append(H2[i + 1].strip('\n').split(':')[1])
            except:
                print("error in compareImgSimilarityFromMANIFEST" + fileName2)
    nx = []
    edge = {}
    cx = {}
    key_index = 0
    simRes = "none"
    if HashVal1.__len__() > 0 and HashVal2.__len__() > 0:
        for hashVal1 in HashVal1:
            hashVal1 = hashVal1.strip('\n')
            key_i = 0
            edge_y = {}
            for hashVal2 in HashVal2:
                hashVal2 = hashVal2.strip('\n')
                # dist = hamming_distance_with_hash(hashVal1,hashVal2)
                # if dist <= 5:
                #     edge_y[key_i] = 1 # 1 表示可以匹配， 0 表示不能匹配
                #     key_i = key_i + 1
                # else:
                #     edge_y[key_i] = 0
                #     key_i = key_i + 1
                if hashVal1 == hashVal2:
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
        for hashVal2 in HashVal2:
            cy[key_i] = -1
            visited[key_i] = 0
            ny.append(key_i)
            key_i = key_i + 1
        simRes = HungarianAlgorithm(nx, ny, edge, cx, cy, visited).max_match()
        simRes = simRes / min(HashVal1.__len__(),HashVal2.__len__())

        #四舍五入
        simRes =str(float(Decimal(simRes).quantize(Decimal('0.000'))))
    else:        #如果有的APK文件下没有相关的签名的话直接判定为可疑重打包应用
        simRes = 1
    return str(simRes)


#hash值之间的汉明距离
def hamming_distance_with_hash(dhash1, dhash2):
    difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
    return bin(difference).count("1")


if __name__ == '__main__':

    f1 = r'C:\Users\Song\Desktop\Desktop\qqq\me.ele\original\META-INF\MANIFEST.MF'
    f2 = r'C:\Users\Song\Desktop\Desktop\qqq\com.mydream.wifi.fromXiaomi\original\META-INF\MANIFEST.MF'

    compareImgSimilarityFromMANIFEST(f1,f2)
