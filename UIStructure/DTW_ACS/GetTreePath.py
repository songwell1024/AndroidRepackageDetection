#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: GetTreePath.py
@time: 2018/12/20/020 16:17
@desc:获取树的路径
'''

import xml.etree.ElementTree as ET

# #获取信息
# def getXmlData(file_name):
#     level = 0  # 节点的深度从1开始
#     result_list = []
#     root = ET.parse(file_name).getroot()
#     walkData(root, level, result_list)
#     return result_list
#
# #遍历xml
# def walkData(root_node, level, result_list):
#     if (root_node.attrib.__contains__('class')):
#         if root_node.attrib['visible-to-user'] == 'false':
#             return
#         temp_list = [level, root_node.attrib['class']]
#         if (root_node.attrib.__contains__('clickable')):
#             temp_list.append(root_node.attrib['clickable'])
#         if (root_node.attrib.__contains__('checkable')):
#             temp_list.append(root_node.attrib['checkable'])
#         if (root_node.attrib.__contains__('bounds')):
#             temp_list.append(root_node.attrib['bounds'])
#         result_list.append(temp_list)
#
#     # 遍历每个子节点
#     children_node = root_node.getchildren()
#     if len(children_node) == 0:
#         return
#     for child in children_node:
#         if child.tag == 'node':
#             walkData(child, level + 1, result_list)
#     return


def walkData(root_node, level, result_list):
    key = '{http://schemas.android.com/apk/res/android}visibility'
    if root_node.attrib.__contains__(key) and (                #过滤掉不可见的点
            root_node.attrib[key] == 'invisible' or root_node.attrib[key] == 'gone'):
        return
    temp_list = [level, root_node.tag]
    result_list.append(temp_list)

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        print(result_list)
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

def getAllSubPathOfTree(file_name):
    result_list = getXmlData(file_name)
    index = 0;
    while(index < result_list.__len__()):
        de


def getStrXmlMap(file_name):
    StrXml = ""
    level = 1
    for node in getXmlData(file_name):
        str = node[1]
        if str.find(".") != -1 and str.find('android.support.') != -1:
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