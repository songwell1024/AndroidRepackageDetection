#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: GetXmlInformation.py
@time: 2018/11/26/026 14:33
@desc: 获取xml文件树的所有路径
每个节点不只取他的节点，还取他的属性
取得属性不包括index，text,resource-id,package,content-desc,bounds
其余属性全部包括
同时对button节点中的password属性永远不可能为true，所以对于是button的属性password也全部过滤掉
同时有人可能会添加不可见的布局属性，这样不改变外观但是改变了xml的结构，
这种属性的节点就直接过滤掉比如visible-to-user=false（不可见），visible-to-user=gone(隐藏)等属性
'''

import xml.etree.ElementTree as ET
from treelib import Node, Tree

index_node = 0

def walkData(root_node, parent_node_id, tree):
    global index_node
    if parent_node_id == "":
        if root_node.attrib.__contains__('class'):
            node = root_node.attrib['class']+ ':' + root_node.attrib['checkable'] + ':' + root_node.attrib['checked'] + ':' \
            + root_node.attrib['clickable'] +':' + root_node.attrib['enabled'] +':' + root_node.attrib['focusable'] \
            +':' + root_node.attrib['focused'] +':' + root_node.attrib['scrollable'] +':' + root_node.attrib['long-clickable'] \
            + ':' + root_node.attrib['selected']
            if not (root_node.attrib['class'].__contains__('Button') or root_node.attrib['class'].__contains__('button')):
                node = node + ':'+ root_node.attrib['password']
            else:
                node = node + ':' + 'null'
            node = node + ':'+ root_node.attrib['visible-to-user']
        else:
            node = root_node.tag
        root_node_id = node + str(index_node)
        tree.create_node(node,root_node_id)
    else:
        if root_node.attrib.__contains__('class'):
            node = root_node.attrib['class'] + ':' + root_node.attrib['checkable'] + ':' + root_node.attrib[
                'checked'] + ':' \
                   + root_node.attrib['clickable'] + ':' + root_node.attrib['enabled'] + ':' + root_node.attrib[
                       'focusable'] \
                   + ':' + root_node.attrib['focused'] + ':' + root_node.attrib['scrollable'] + ':' + root_node.attrib[
                       'long-clickable'] \
                   + ':' + root_node.attrib['selected']
            if not (root_node.attrib['class'].__contains__('Button') or root_node.attrib['class'].__contains__('button')):
                node = node + ':' + root_node.attrib['password']
            else:
                node = node + ':' + 'null'
            node = node + ':' + root_node.attrib['visible-to-user']
        else:
            node = root_node.tag
        root_node_id = node + str(index_node)
        tree.create_node(node,root_node_id, parent = parent_node_id)
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
    treePaths_id_list = tree.paths_to_leaves()  #树的数据路径
    treePaths_list = []
    for paths in treePaths_id_list :
        path_list = []
        for i in range(1, paths.__len__()):
            path = paths[i]
            path = removeLastIntegerNumber(path)
            if path.endswith('true', path.__len__() - 4, path.__len__()):
                path_list.append(path)
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