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

def dataPeocessAndShow(fileName):
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    if os.path.exists(fileName):
        f = open(fileName)
        valList = f.readlines()
        f.close()
        i= 1
        for val in  valList:
            val = val.strip('\n')
            strList = val.split(' ')
            # if strList[strList.__len__() - 1] != "10" and strList[strList.__len__() - 2] != "10":
            if strList[strList.__len__() - 1] != "none" and strList[strList.__len__() - 2] != "none":
                ycord1.append(float(strList[strList.__len__() - 1]))
                xcord1.append(i)
                ycord2.append(float(strList[strList.__len__() - 2]))
                xcord2.append(i)
                i = i + 1
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
        ax.scatter(ycord1, ycord2, s=1, c='red')
        plt.xlabel('CompPerm')
        plt.ylabel('imghash')
        plt.show()
    else:
        print("There is no such file ")