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


def getStrXml(file_name):
    StrXml = ""
    level = 1
    for node in getXmlData(file_name):
        if level < node[0]:
            level = node[0]
            StrXml = StrXml + "(" + node[1]
        elif level > node[0]:
            for i in range(level - node[0]):
                StrXml = StrXml + ")"
            level = node[0]
            StrXml = StrXml + "," + node[1]
        else:
            if StrXml.strip() != '':
                StrXml = StrXml + "," + node[1]
            else:
                StrXml = node[1]
    for i in range(level - 1):
        StrXml = StrXml + ")"
    return StrXml

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