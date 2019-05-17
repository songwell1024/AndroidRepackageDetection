#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: DataProcessAndShow.py
@time: 2019/1/15 10:18
@desc: 数据展示
'''

from numpy import *
import matplotlib.pyplot as plt
import os

def dataPeocessAndShow(fileName1,fileName2):
    xcord1 = []
    ycord1 = []
    if os.path.exists(fileName1):
        f = open(fileName1)
        valList = f.readlines()
        f.close()
        for val in  valList:
            val = val.strip('\n')
            strList = val.split(' ')
            if strList[strList.__len__() - 1] != "10" and strList[strList.__len__() - 2] != "10":
                xcord1.append(float(strList[strList.__len__() - 1]))   #compent
                ycord1.append(float(strList[strList.__len__() - 2]))   #image
    xcord2 = []
    ycord2 = []
    if os.path.exists(fileName2):
        f = open(fileName2)
        valList = f.readlines()
        f.close()
        for val in valList:
            val = val.strip('\n')
            strList = val.split(' ')
            if strList[strList.__len__() - 1] != "none" and strList[strList.__len__() - 2] != "none":
                xcord2.append(float(strList[strList.__len__() - 1]))       ##compent
                ycord2.append(float(strList[strList.__len__() - 2]))       #image

        # 资源哈希和组件的组
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(ycord1, xcord1, s=3, c='red', marker='*')
        ax.scatter(ycord2, xcord2, s=3, c='green',marker='s')
        plt.xlabel('imghash')
        plt.ylabel('CompPerm')
        plt.show()

        # 组件的图
        le1 = xcord1.__len__()
        y1 = []
        for i in range(le1):
            y1.append(i)

        le11 = xcord2.__len__()
        y11 = []
        for i in range(le11):
            y11.append(i)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        # ax.scatter(y1, xcord1, s=2, c='red')
        ax.scatter(y1, xcord1, s=2, c='red',marker='*')
        ax.scatter(y11, xcord2, s=2, c='green',marker='s')
        plt.xlabel('APP')
        plt.ylabel('CompPerm')
        plt.show()

        # 资源哈希的图
        le2 = ycord1.__len__()
        y2 = []
        for i in range(le2):
            y2.append(i)

        le22 = ycord2.__len__()
        y22 = []
        for i in range(le22):
            y22.append(i)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # ax.scatter(y2, ycord1, s=2, c='red')
        ax.scatter(y2, ycord1,s=2, c='red',marker='*')
        ax.scatter(y22, ycord2, s=2, c='green',marker='s')
        plt.xlabel('APP')
        plt.ylabel('Iamge Hash')
        plt.show()

    else:
        print("There is no such file ")