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

filename = r'C:\Users\Song\Desktop\val2\trainData.txt'  # 文件目录

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
    xcord1 = []
    ycord1 = []
    xcord2 = []
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
    x = arange(0, 1.1, 0.1)
    y = (-weights[0]-weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


###############################################################################################################################
###数据预测
# classifyVector的第一个参数为回归系数,weight为特征向量，这里将输入这两个参数来计算sigmoid值，如果只大于0.5，则返回1，否则返回0.
def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5:
        return 1.0  # 如果不想得到分类，则直接返回prob概率
    else:
        return 0.0


# 打开数据集并对数据集进行处理
def colicTest():
    frTrain = open(filename)
    frTest = open(filename)
    trainingSet = []
    trainingLabels = []

    # 获取训练集的数据，并将其存放在list中
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []  # 用于存放每一行的数据
        for i in range(2):  # 这里的range(21)是为了循环每一列的值，总共有22列
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent1(array(trainingSet), trainingLabels, 1000)  # 用改进的随机梯度算法计算回归系数

    # 计算测试集的错误率
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(3):
            lineArr.append(float(currLine[i]))
            # 如果预测值和实际值不相同，则令错误个数加1
        if int(classifyVector(array(lineArr), trainWeights)) != int(currLine[2]):
            errorCount += 1
    errorRate = (float(errorCount) / numTestVec)  # 最后计算总的错误率
    print("the error rate of this test is: %f" % errorRate)
    return errorRate


# 调用coicTest函数10次并求平均值
def multiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print("after %d iterations the average error rate is: %f" % (numTests, errorSum / float(numTests)))

if __name__ == '__main__':
    # dataMat, labelMat = loadDataSet()
    # weights = stocGradAscent1(dataMat, labelMat).getA()
    # plotBestFit(weights)
    colicTest()

