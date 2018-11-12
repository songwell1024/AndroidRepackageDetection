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

# 遍历所有的节点
def walkData(root_node, level, result_list):
    temp_list = [level, root_node.tag]
    result_list.append(temp_list)

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, level + 1, result_list)
    return


def getXmlData(file_name):
    level = 1  # 节点的深度从1开始
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, level, result_list)
    return result_list


def getStrXmlMap(file_name, EleDict):
    StrXml = ""
    level = 1
    for node in getXmlData(file_name):
        str = node[1]
        if str.find(".") != -1:
            str = str.split('.')[-1]
        if level < node[0]:
            level = node[0]
            StrXml = StrXml + "(" + elementMap(str, EleDict)
        elif level > node[0]:
            for i in range(level - node[0]):
                StrXml = StrXml + ")"
            level = node[0]
            StrXml = StrXml + "," + elementMap(str, EleDict)
        else:
            if StrXml.strip() != '':
                StrXml = StrXml + "," + elementMap(str, EleDict)
            else:
                StrXml = elementMap(str, EleDict)
    for i in range(level - 1):
        StrXml = StrXml + ")"
    return StrXml


##################################################
def getStrXml(file_name):
    StrXml = ""
    level = 1
    for node in getXmlData(file_name):
        str = node[1]
        if str.find(".") != -1:
            str = str.split('.')[-1]
        if level < node[0]:
            level = node[0]
            StrXml = StrXml + "(" + str
        elif level > node[0]:
            for i in range(level - node[0]):
                StrXml = StrXml + ")"
            level = node[0]
            StrXml = StrXml + "," + str
        else:
            if StrXml.strip() != '':
                StrXml = StrXml + "," + str
            else:
                StrXml = str
    for i in range(level - 1):
        StrXml = StrXml + ")"
    return StrXml
##################################################

def getTreeFromXmlPath(filePath):
    wrong_cnt = 0
    for anno_xml in glob.glob(os.path.join(filePath, '*')):
        if anno_xml.endswith('.xml'):
            try:
                strXml = getStrXml(anno_xml)
                print(strXml)
            except Exception as e:
                print("Error: cannot parse file: %s" % anno_xml)
                wrong_cnt += 1
                continue

def getMapTreeFromXmlPath(filePath,EleDict):
    wrong_cnt = 0
    for anno_xml in glob.glob(os.path.join(filePath, '*')):
        if anno_xml.endswith('.xml'):
            try:
                strXml = getStrXmlMap(anno_xml,EleDict)
                print(strXml)
            except Exception as e:
                print("Error: cannot parse file: %s" % anno_xml)
                wrong_cnt += 1
                continue


#计算字符串的hash值
def getStrHash(str):
    md5 = hashlib.md5()
    md5.update(bytes(str, encoding='utf-8'))
    return md5.hexdigest()

# 元素映射
def elementMap(str, EleDict):
    if EleDict.get(str) is not None:
        return EleDict.get(str)
    else:
        return "%"
