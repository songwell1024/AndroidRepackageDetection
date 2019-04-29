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

index_node = 0

def walkData(root_node, parent_node_id, tree):
    global index_node
    key = '{http://schemas.android.com/apk/res/android}visibility'
    if root_node.attrib.__contains__(key) and (                #过滤掉不可见的点
            root_node.attrib[key] == 'invisible' or root_node.attrib[key] == 'gone'):
        return
    if parent_node_id == "":
        root_node_id = root_node.tag + str(index_node)
        tree.create_node(root_node.tag,root_node_id)
    else:
        root_node_id = root_node.tag + str(index_node)
        tree.create_node(root_node.tag,root_node_id, parent = parent_node_id)
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
    return treePaths_list


#移除树节点id中我添加的整数index
def removeLastIntegerNumber(node_str):
    list_str = list(node_str)
    for i in range(node_str.__len__() -1, -1, -1):
        if list_str[i] >= "0"  and list_str[i] <= "9":
            list_str.pop(i)
        else:
            break
    node_str = ''.join([str(x) for x in list_str])
    return node_str


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
#
