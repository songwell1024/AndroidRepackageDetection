#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: LogisticRegression.py
@time: 2019/1/3/003 16:54
@desc: 逻辑回归问题
'''
from numpy import *

filename = r'C:\Users\Song\Desktop\AppSimTxt\data.txt'  # 文件目录

def loadDataSet():  # 读取数据（这里只有两个特征）
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])  # 前面的1，表示方程的常量。比如两个特征X1,X2，共需要三个参数，W1+W2*X1+W3*X2
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):  # sigmoid函数
    return 1.0 / (1 + exp(-inX))


def stocGradAscent1(dataMat, labelMat):  # 改进版随机梯度上升，在每次迭代中随机选择样本来更新权重，并且随迭代次数增加，权重变化越小。
    dataMatrix = mat(dataMat)
    classLabels = labelMat
    m, n = shape(dataMatrix)
    weights = ones((n, 1))
    maxCycles = 500
    for j in range(maxCycles):  # 迭代
        dataIndex = [i for i in range(m)]
        for i in range(m):  # 随机遍历每一行
            alpha = 4 / (1 + j + i) + 0.0001  # 随迭代次数增加，权重变化越小。
            randIndex = int(random.uniform(0, len(dataIndex)))  # 随机抽样
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex].transpose()
            del (dataIndex[randIndex])  # 去除已经抽取的样本
    return weights


def plotBestFit(weights):  # 画出最终分类的图
    import matplotlib.pyplot as plt
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = [];
    ycord1 = []
    xcord2 = [];
    ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


if __name__ == '__main__':
    dataMat, labelMat = loadDataSet()
    weights = stocGradAscent1(dataMat, labelMat).getA()
    plotBestFit(weights)

