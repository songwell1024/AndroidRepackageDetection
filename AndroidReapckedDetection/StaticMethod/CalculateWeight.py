#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: CalculateWeight.py
@time: 2019/1/18 15:01
@desc: 初级检测权重的确定
'''
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
from numpy import *
from mpl_toolkits.mplot3d import Axes3D


def calculateWeight(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([float(lineArr[0]), float(lineArr[1])])  # 前面的1，表示方程的常量。比如两个特征X1,X2，共需要三个参数，W1+W2*X1+W3*X2
        labelMat.append(int(lineArr[2]))

    misdiagnosisRates = []   #误报
    omissiveJudgementRates = []  ##漏报
    #threshold  阈值
    #weight 权重
    weightsAndthresholdsArray = []
    weights = np.linspace(0.01, 1, num=100)
    thresholds = np.linspace(0.01, 1, num=100)

    for threshold in thresholds:
        for weight in weights:
            weightsAndthresholdsArray.append([threshold, weight])
            misdiagnosisNum = 0
            omissiveJudgement = 0
            for i in range(1, labelMat.__len__()):
                y = weight * dataMat[i][0] + (1-weight) * dataMat[i][1]
                if y >= threshold:
                    label = 1
                else:
                    label = 0
                if labelMat[i] == 1 and label == 0:   #漏报
                    omissiveJudgement = omissiveJudgement + 1
                if labelMat[i] == 0 and label == 1:  ##误报
                    misdiagnosisNum = misdiagnosisNum + 1
            omissiveJudgementRates.append(float(Decimal(omissiveJudgement / labelMat.__len__()).quantize(Decimal('0.00000000'))))
            misdiagnosisRates.append(float(Decimal(misdiagnosisNum/labelMat.__len__()).quantize(Decimal('0.00000000'))))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(omissiveJudgementRates, misdiagnosisRates, s=10, c='red')

    plt.xlabel('omissiveJudgementRates')
    plt.ylabel('misdiagnosisRates')
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(omissiveJudgementRates, misdiagnosisRates)
    plt.show()

    # minOmissiveJudgementRate = 1
    minMisdiagnosisRate = 1
    weight = 1
    threshold = 1
    omissiveJudgementRate = 1
    for i in range(1, omissiveJudgementRates.__len__()):
        if omissiveJudgementRates[i] == 0:
            omissiveJudgementRate = omissiveJudgementRates[i]
            if misdiagnosisRates[i] < minMisdiagnosisRate:
                minMisdiagnosisRate = misdiagnosisRates[i]
                threshold = weightsAndthresholdsArray[i][0]
                weight = weightsAndthresholdsArray[i][1]


    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    xcord3 = []
    ycord3 = []
    for i in range(1, labelMat.__len__()):
        y = weight * dataMat[i][0] + (1 - weight) * dataMat[i][1]
        if y >= threshold:
            label = 1
        else:
            label = 0
        if labelMat[i] == 0 and label == 0:  ##正常的
            xcord1.append(dataMat[i][0])
            ycord1.append(dataMat[i][1])
        if labelMat[i] == 1 and label == 1:  ##正常的
            xcord2.append(dataMat[i][0])
            ycord2.append(dataMat[i][1])
        if labelMat[i] == 0 and label == 1:  # 误报的
            xcord3.append(dataMat[i][0])
            ycord3.append(dataMat[i][1])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=5, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=5, c='green',marker='o')
    ax.scatter(xcord3, ycord3, s=5, c='black', marker='*')
    x = arange(0, 1.1, 0.01)
    y = (threshold - weight * x) / (1-weight)
    ax.plot(x, y)
    plt.show()

    xcord4 = []
    ycord4 = []
    zcord4 = []
    for i in range(omissiveJudgementRates.__len__()):
        xcord4.append(weightsAndthresholdsArray[i][0])
        ycord4.append(weightsAndthresholdsArray[i][1])
        zcord4.append(omissiveJudgementRates[i])
    fig = plt.figure()
    ax = Axes3D(fig)
    # ax = fig.add_subplot(111)
    ax.plot_surface(xcord4, ycord4, zcord4, rstride=1, cstride=1, cmap='rainbow')  # 绘面
    plt.show()



    return threshold, weight, omissiveJudgementRate, minMisdiagnosisRate




if __name__ == "__main__":
    fileName = r'C:\Users\Song\Desktop\val2\trainData.txt'  # 文件目录
    threshold, weight ,omissiveJudgementRate, minMisdiagnosisRate = calculateWeight(fileName)
    print(threshold, weight ,omissiveJudgementRate, minMisdiagnosisRate)