#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: processSml.py.py
@time: 2018/11/6/007 15:52
@desc: 读取辅助特征向量，然后使用余弦相似度比较辅助特征的相似度
'''

import xml.etree.ElementTree as ET
import os

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

#获取文件目录下的所有子文件下的APP的辅助特征向量
def getAccessorialVectorOfApp(filePath):
    getElementFrequency(filePath)

#获取APP文件下的向量
def getElementFrequency(filePath):
    # print("<permission,permission,activity,receiver,provider,service,resCount,assetsCount,libCount,fileCount>")
    dirList = os.listdir(filePath)
    for i in range(len(dirList)):  # 得到apk 文件夹下的每一个子的类别
        vectorFileName = filePath + "\\" + dirList[i] + "\\AccessorialVector.txt"
        if os.path.exists(vectorFileName):
            os.remove(vectorFileName)
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
        vecStr = str(EFreqArr)
        writeToTxt(vecStr, vectorFileName)


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
        if EFreq.__contains__(i):
            res.append(EFreq[i])
        else:
            res.append(0)
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