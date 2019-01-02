#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: processSml.py.py
@time: 2018/11/6/007 15:52
@desc: 遍历XML文件并将树结构抽象成字符串
'''

import xml.etree.ElementTree as ET
import glob
import os
import hashlib
import numpy

# 遍历所有的节点
def walkData(root_node, result_list):
    str = root_node.tag
    if str.find(".") != -1:
        str = str.split('.')[-1]
    result_list.append(str)

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, result_list)
    return


def getXmlData(file_name):
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, result_list)
    return result_list


def getElementFrequency(filePath):
    vectorFileName = r'C:\Users\Administrator\Desktop\AndroidManifestTxt\AndroidManifestTxt.txt'
    if os.path.exists(vectorFileName):
        os.remove(vectorFileName)
    print("<permission,permission,activity,receiver,provider,service,resCount,assetsCount,libCount,fileCount>")
    dirList = os.listdir(filePath)
    for i in range(len(dirList)):  # 得到apk 文件夹下的每一个子的类别
        EFreq = {}
        wrong_cnt = 0
        file_xml = filePath + "\\" + dirList[i] + "\\AndroidManifest.xml"
        try:
            ArrXml =getXmlData(file_xml)
            arrayToDict(EFreq, ArrXml)
        except Exception as e:
            print("Error: cannot parse file: %s" % file_xml)
            wrong_cnt += 1
            continue
        EFreqArr = MapToVector(EFreq)

        resCount = getFileNumber(filePath + "\\" + dirList[i] + "\\res")
        EFreqArr.append(resCount)
        assetsCount = getFileNumber(filePath + "\\" + dirList[i] + "\\assets")
        EFreqArr.append(assetsCount)
        libCount = getFileNumber(filePath + "\\" + dirList[i] + "\\lib")
        EFreqArr.append(libCount)
        fileCount = getFileNumber(filePath + "\\" + dirList[i])
        EFreqArr.append(fileCount)
        vecStr = dirList[i] + ":" + str(EFreqArr)
        writeToTxt(vecStr, vectorFileName)
        # print(dirList[i] + ":  ", EFreqArr)


#遍历数组中的元素获取出现的频率
def arrayToDict(EleFrequ, EleArr):
    for str in EleArr:
        if EleFrequ.__contains__(str):
            EleFrequ[str] = EleFrequ[str] + 1
        else:
            EleFrequ[str] = 1


def MapToVector(EFreq):
    ele = ['uses-permission','permission','activity','receiver','provider','service']
    res = []
    for i in ele:
        res.append(EFreq[i])
    return res

def getFileNumber(filePath):
    fileNum = 0;
    if os.path.exists(filePath):
        for dirList, folderList, fileList in os.walk(filePath):
            fileNum += len(fileList)
    return fileNum


def writeToTxt(str,fileName):
    f = open(fileName, 'a')
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close


#从文件中读取并进行相似性的比较
def readTxtToArrayAndCompareSimilarity(fileName):
    if os.path.exists(fileName):
        f  = open(fileName)
        contents = f.readlines();
        for i in (range(len(contents)-1)):
            contents[i] = contents[i].strip('\n')
            strArr_i = contents[i].split(':')
            vectorArr_i = strToArr(strArr_i[1])
            for j in range(i+1, len(contents)):
                contents[j] = contents[j].strip('\n')
                strArr_j = contents[j].split(':')
                vectorArr_j = strToArr(strArr_j[1])
                print(strArr_i[0] + ' and ' + strArr_j[0]+ ':  ',cosSimilarity(vectorArr_i,vectorArr_j))
    else:
            print("There is no such file")


#字符串转换为数组 ------> '[1,2,3]'---> [1,2,3]
def strToArr(str):
    resArr = []
    strArr = str.split(',')
    for i in range(len(strArr)):
        if i == 0:
            strArr[i] = strArr[i].strip('[')
        if i == (len(strArr) - 1):
            strArr[i] = strArr[i].strip(']')
        resArr.append(float(strArr[i]))
    return resArr


#余弦相似度
def cosSimilarity(arr1, arr2):
    if len(arr1) != len(arr2):
        return 0
    denominator1 = 0
    denominator2 = 0
    numerator = 0
    for i in range(len(arr1)):
        numerator += arr1[i] * arr2[i]
        denominator1 += numpy.square(arr1[i])
        denominator2 += numpy.square(arr2[i])
    return (numerator / (numpy.sqrt(denominator1) * numpy.sqrt(denominator2)))
