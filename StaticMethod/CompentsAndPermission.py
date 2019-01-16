#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: CompentsAndPermission.py
@time: 2019/1/9/009 16:24
@desc: 组件和权限的提取
'''

import xml.etree.ElementTree as ET
import glob
import os
import hashlib
import numpy

# 遍历所有的节点
def walkData(root_node, result_dict):
    str = root_node.tag
    if str == "uses-permission" or str == "uses-feature" or str == "permission":        #官方权限
        key = '{http://schemas.android.com/apk/res/android}name'
        if root_node.attrib.__contains__(key):
            value = root_node.attrib[key];
            newKey = root_node.tag + ":" + value;
            result_dict[newKey] = "none"
    elif str == "activity" or str == "receiver" or str == "provider" or str == "service":     #自定义权限
        key = '{http://schemas.android.com/apk/res/android}name'
        if root_node.attrib.__contains__(key):
            value = root_node.attrib[key];
            newKey = root_node.tag + ":" + value;
            children_node = root_node.getchildren()
            newVal = ""
            if len(children_node) != 0:
                for child in  children_node:
                    if child.tag == "intent-filter":
                        if newVal != "":
                            newVal = newVal + ","
                        grandChildren = child.getchildren()
                        for grandChild in grandChildren:
                            if grandChild.tag == "action" :
                                if newVal != "" and newVal[-1] != ",":
                                    newVal = newVal + ":"
                                newVal = newVal + grandChild.attrib[key]
                            elif grandChild.tag == "category":
                                newVal = newVal + "/" + grandChild.attrib[key]
            result_dict[newKey] = newVal
    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, result_dict)
    return


def getXmlData(file_name):
    result_dict = {}
    root = ET.parse(file_name).getroot()
    walkData(root, result_dict)
    return result_dict


# def getElementFrequency(filePath):
def getElementFrequency(fileName):
    dict = getXmlData(fileName)
    return dict

def writeToTxt(str,fileName):
    f = open(fileName, 'a')
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close


