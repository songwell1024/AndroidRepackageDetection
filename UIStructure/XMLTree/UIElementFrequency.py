#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: UIElementFrequency.py.py
@time: 2018/11/7/007 15:52
@desc:遍历XML文件下组件元素出现的频率
'''

import xml.etree.ElementTree as ET
import glob
import os

# 遍历所有的节点
def walkData(root_node, result_list):
    str = root_node.tag
    if str.find(".") != -1 and str.find('android.support.') != -1:
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


def getUIElementFrequency(filePath):
    dirList = os.listdir(filePath)
    for i in range(len(dirList)):  # 得到apk 文件夹下的每一个子的类别
        fileList = filePath + "\\" + dirList[i] + "\\res\\layout" # 获取每个类别的路径
        elementFrequencyTxt = filePath + "\\" + dirList[i] + "\\"+ "elementFrequency.txt"
        EFrequ = {}
        wrong_cnt = 0
        for file_xml in glob.glob(os.path.join(fileList, '*')):
            if file_xml.endswith('.xml'):
                try:
                    ArrXml =getXmlData(file_xml)
                    arrayToDict(EFrequ, ArrXml)
                except Exception as e:
                    print("Error: cannot parse file: %s" % file_xml)
                    wrong_cnt += 1
                    continue
        # 将字典排序
        EFreq = sorted(EFrequ.items(), key=lambda item: item[1], reverse=True)
        EFreqList = getElementPer(EFreq)
        file_handle = open(elementFrequencyTxt, mode='w')
        ## 不做预处理直接把映射的特征向量写入text文件
        for e in EFreqList:
            s = ' '.join(e)
            file_handle.write(s)
            file_handle.write('\n')
        file_handle.close()


#遍历数组中的元素获取出现的频率
def arrayToDict(EleFrequ, EleArr):
    for str in EleArr:
        if EleFrequ.__contains__(str):
            EleFrequ[str] = EleFrequ[str] + 1
        else:
            EleFrequ[str] = 1


#获取出现频率的百分比
def getElementPer(strArr):
    sum = 0     #求和
    res = []  #返回的数组
    for i in strArr:
        sum += i[1]
    for i in strArr:
        res.append([i[0],str(i[1] / sum)])
    return res
