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
from treelib import Node, Tree
import os

index_node = 0

def walkData(root_node, parent_node_id, tree):
    global index_node
    key = '{http://schemas.android.com/apk/res/android}visibility'
    if root_node.attrib.__contains__(key) and (                #过滤掉不可见的点
            root_node.attrib[key] == 'invisible'):
        return
    if parent_node_id == "":
        if root_node.tag == 'include':
            root_node_id = root_node.tag +':'+ root_node.attrib['layout'] + str(index_node)
            tree.create_node(root_node.tag,root_node_id)
        else:
            root_node_id = root_node.tag + str(index_node)
            tree.create_node(root_node.tag, root_node_id)
    else:
        if root_node.tag == 'include':
            root_node_id = root_node.tag +':'+ root_node.attrib['layout'] + str(index_node)
            tree.create_node(root_node.tag,root_node_id, parent = parent_node_id)
        else:
            root_node_id = root_node.tag + str(index_node)
            tree.create_node(root_node.tag, root_node_id, parent=parent_node_id)
    index_node = index_node + 1

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, root_node_id, tree)
    return

def getAllSubPathOfTree(file_name):
    global index_node
    index_node = 0
    parent_node = ""
    tree = Tree()
    root = ET.parse(file_name).getroot()
    walkData(root, parent_node, tree)
    treePaths_id_list = tree.paths_to_leaves()  #映射成为树的节点的ID形成的路径，和树的数据的路径还不大一样
    treePaths_list = []
    for paths in treePaths_id_list :
        path_list = []
        for path in paths:
            path_list.append(removeLastIntegerNumber(path))
        treePaths_list.append(path_list)
    ## 这里要处理include的属性
    filePath = os.path.dirname(os.path.realpath(file_name))  #获取当前文件所在文件夹
    resTreePaths_list = addIncludeXMlTree(treePaths_list, filePath)
    print(treePaths_list)
    return resTreePaths_list

#移除树节点id中添加的整数index
def removeLastIntegerNumber(node_str):
    list_str = list(node_str)
    for i in range(node_str.__len__() -1, -1, -1):
        if list_str[i] >= "0"  and list_str[i] <= "9":
            list_str.pop(i)
        else:
            break
    node_str = ''.join([str(x) for x in list_str])
    return node_str


##处理包含在xml中的include中的属性,也就是一个xml文件中可能包含很多的其他的xml文件中的内容
##这里的意思可能就是每一个Android应用可能包含很多的公共的布局属性，供使用
def addIncludeXMlTree(treePaths_list, filePath):
    resTreePathsList = []
    for treePath in treePaths_list:
        if treePath[treePath.__len__()-1].__contains__('include'):
            IncludeXMLFileName = filePath + "\\" + treePath[treePath.__len__()-1].split('/')[1] + '.xml'
            includeTreePaths = getAllSubPathOfTree(IncludeXMLFileName)
            for itp in  includeTreePaths:
                help = []
                for i in  range(treePath.__len__()-1):
                    help.append(treePath[i])
                for j in itp:
                    help.append(j)
                resTreePathsList.append(help)
        else:
            resTreePathsList.append(treePath)
    return resTreePathsList