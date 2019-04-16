#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: DataProcessAndShow.py
@time: 2019/1/15 10:18
@desc:
'''

from numpy import *
import matplotlib.pyplot as plt
import os

def dataPeocessAndShow(fileName1,fileName2):
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    if os.path.exists(fileName1):
        f = open(fileName1)
        valList = f.readlines()
        f.close()
        for val in  valList:
            val = val.strip('\n')
            strList = val.split(' ')
            if strList[strList.__len__() - 1] != "10" and strList[strList.__len__() - 2] != "10":
            # if strList[strList.__len__() - 1] != "none" and strList[strList.__len__() - 2] != "none":
                xcord1.append(float(strList[strList.__len__() - 1]))
                ycord1.append(float(strList[strList.__len__() - 1]))
                xcord2.append(float(strList[strList.__len__() - 2]))
                ycord2.append(float(strList[strList.__len__() - 2]))
    xcord3 = []
    ycord3 = []
    xcord4 = []
    ycord4 = []
    if os.path.exists(fileName2):
        f = open(fileName2)
        valList = f.readlines()
        f.close()
        for val in valList:
            val = val.strip('\n')
            strList = val.split(' ')
            # if strList[strList.__len__() - 1] != "10" and strList[strList.__len__() - 2] != "10":
            if strList[strList.__len__() - 1] != "none" and strList[strList.__len__() - 2] != "none":
                xcord3.append(float(strList[strList.__len__() - 1]))
                ycord3.append(float(strList[strList.__len__() - 1]))
                xcord4.append(float(strList[strList.__len__() - 2]))
                ycord4.append(float(strList[strList.__len__() - 2]))
        #组件的图
        fig = plt.figure()
        # ax = fig.add_subplot(131)
        ax = fig.add_subplot(111)
        # ax.scatter(xcord1, ycord1, s=1, c='red', marker='s')
        ax.scatter(xcord1, ycord1, s=1, c='red')
        plt.xlabel('CompPerm')
        plt.ylabel('CompPerm')
        plt.show()

        #资源哈希的图
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(xcord2, ycord2, s=1, c='red')
        plt.xlabel('imghash')
        plt.ylabel('imghash')
        plt.show()

        # 资源哈希和组件的组
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(xcord1, ycord2, s=10, c='red', marker='*')
        ax.scatter(xcord3, ycord4, s=10, c='green',marker='s')
        plt.xlabel('CompPerm')
        plt.ylabel('imghash')
        plt.show()

        le1 = xcord1.__len__()
        y1 = []
        for i in range(le1):
            y1.append(i)
        le2 = xcord2.__len__()
        y2 = []
        for i in range(le2):
            y2.append(i)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(y1, xcord1,s=2, c='red')
        plt.xlabel('APP')
        plt.ylabel('CompPerm')
        plt.show()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(y2, xcord2,s=2, c='red')
        plt.xlabel('APP')
        plt.ylabel('CompPerm')
        plt.show()

    else:
        print("There is no such file ")