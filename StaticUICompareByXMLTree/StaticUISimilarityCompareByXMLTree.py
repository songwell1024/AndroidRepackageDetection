#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: GetTreePath.py
@time: 2018/12/20/020 16:17
@desc:静态UI的相似性比较
'''

import StaticUICompareByXMLTree.ACS as ACS
import StaticUICompareByXMLTree.dtwAcs as dtwAcs
import StaticUICompareByXMLTree.GetTreePath as GTP
from StaticMethod.HungarianAlgorithm import HungarianAlgorithm
import os
from decimal import Decimal


#两两比较的方式，存储的方式
#先获取到file_path下的目录下的所有文件夹，每个文件夹下存储的是要比较的两个应用的xml文件
#同时这里使用了匈牙利最大匹配算法
def StaticUISimilarityCompareByXMLTree(file_path, APPSimText):
    file_path_lists = os.listdir(file_path)
    for path in file_path_lists:
        app_paths = os.listdir(file_path + '\\' + path)
        xml_paths1 = file_path + '\\' + path +'\\' + app_paths[0] + '\\' + "res" + '\\' + "layout"
        xml_paths2 = file_path + '\\' + path + '\\' + app_paths[1] + '\\' + "res" + '\\' + "layout"
        xml_list1 = os.listdir(xml_paths1)
        xml_list2 = os.listdir(xml_paths2)
        nx = []
        edge = {}
        cx = {}
        key_index = 0
        simRes = "none"
        for xml1 in xml_list1:
            xmlFileName1 = xml_paths1 + '\\' + xml1
            treePathsOfXmlFileName1 = GTP.getAllSubPathOfTree(xmlFileName1)
            key_i = 0
            edge_y = {}
            for xml2 in xml_list2:
                xmlFileName2 = xml_paths2 + '\\' + xml2
                treePathsOfXmlFileName2 = GTP.getAllSubPathOfTree(xmlFileName2)
                editence = dtwAcs.DTW_ACS(ACS.getSimilarityByAcs(treePathsOfXmlFileName1, treePathsOfXmlFileName2))  # 树的距离
                simOfTwoXmlFile = (max(treePathsOfXmlFileName1.__len__(), treePathsOfXmlFileName2.__len__()) - editence) / max(treePathsOfXmlFileName1.__len__(), treePathsOfXmlFileName2.__len__())  # xml文件树的相似度
                if simOfTwoXmlFile >=0.7:                     #两棵树的相似度大于0.7就认为是相似的
                    edge_y[key_i] = 1  # 1 表示可以匹配， 0 表示不能匹配
                    key_i = key_i + 1
                else:
                    edge_y[key_i] = 0
                    key_i = key_i + 1

            edge[key_index] = edge_y
            cx[key_index] = -1
            nx.append(key_index)
            key_index = key_index + 1

        ny = []
        cy = {}
        visited = {}
        key_i = 0
        for i in xml_list2:
            cy[key_i] = -1
            visited[key_i] = 0
            ny.append(key_i)
            key_i = key_i + 1
        simRes = HungarianAlgorithm(nx, ny, edge, cx, cy, visited).max_match()
        simRes = simRes / min(xml_list1.__len__(), xml_list2.__len__())

        # 四舍五入
        simRes = str(float(Decimal(simRes).quantize(Decimal('0.000'))))
        res = app_paths[0] + "," + app_paths[1] + ":" + simRes
        writeToTxt(res, APPSimText)    #将相似性写入文件


#写入文件
def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close


if __name__ == '__main__':
    # # filename = r'C:\Users\Song\Desktop\AppXml\com.mydream.wifi\com.wifibanlv.wifipartner.activity.MainActivity_0_0.xml'
    # filename = r'C:\Users\Song\Desktop\AppXml\com.mydream.wifi\test.xml'
    # treePath = GTP.getAllSubPathOfTree(filename)
    # print(treePath)
    file_path = r'C:\Users\Song\Desktop\test'
    outTxt = r'C:\Users\Song\Desktop\AppXml\sim.txt'
    StaticUISimilarityCompareByXMLTree(file_path,outTxt)