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
from threading import Timer
from decimal import Decimal


#两两比较的方式，存储的方式
#先获取到file_path下的目录下的所有文件夹，每个文件夹下存储的是要比较的两个应用的xml文件
#同时这里使用了匈牙利最大匹配算法
def StaticUISimilarityCompareByXMLTree(AppSimFile,file_path, scoreTxt,APPSimText,ProblemTxt):
    f = open(AppSimFile, encoding='UTF-8-sig')
    apkList = f.readlines()
    for path in apkList:
        apkHelp = path.split(':')[0]
        # print(apkHelp)
        apk = apkHelp.split(',')
        apkName1 = apk[0]
        apkName2 = apk[1]

        xml_paths1 = file_path + '\\' + apkName1 + '\\' + "res" + '\\' + "layout"
        xml_paths2 = file_path + '\\' + apkName2 + '\\' + "res" + '\\' + "layout"
        try:
            xml_list1 = os.listdir(xml_paths1)
        except:
            xml_list1 = []
            writeToTxt(apkHelp,ProblemTxt)
            # print(apkName1)
        try:
            xml_list2 = os.listdir(xml_paths2)
        except:
            xml_list2 = []
            writeToTxt(apkHelp, ProblemTxt)
            # print(apkName2)
        if xml_list1.__len__() == 0 or xml_list2.__len__() == 0 :
            continue
        if (xml_list1.__len__() <= 200 or xml_list2.__len__() <= 200)\
            and ((xml_list1.__len__()* 3) < (xml_list2.__len__())\
                or xml_list1.__len__() > (xml_list2.__len__() * 3)):
            continue
        if (xml_list1.__len__() > 200 and xml_list2.__len__() > 200)\
            and ((xml_list1.__len__() + 200) < (xml_list2.__len__())\
                or xml_list1.__len__() > (xml_list2.__len__() + 200)):
            continue
        if (xml_list1.__len__() > 1000 and xml_list2.__len__() > 1000):
            print(apkHelp)
            continue
        CompareXmlTree(xml_list1, xml_list2, xml_paths1, xml_paths2, apkName1, apkName2, APPSimText, scoreTxt)

def CompareXmlTree(xml_list1,xml_list2,xml_paths1,xml_paths2,apkName1,apkName2,APPSimText,scoreTxt):
    nx = []
    edge = {}
    cx = {}
    key_index = 0
    simRes = "0.0"
    for xml1 in xml_list1:
        xmlFileName1 = xml_paths1 + '\\' + xml1
        try:
            treePathsOfXmlFileName1 = GTP.getAllSubPathOfTree(xmlFileName1)
        except:
            # print("get tree paths error in " + xmlFileName1)
            treePathsOfXmlFileName1 = []
        key_i = 0
        edge_y = {}
        for xml2 in xml_list2:
            xmlFileName2 = xml_paths2 + '\\' + xml2
            try:
                treePathsOfXmlFileName2 = GTP.getAllSubPathOfTree(xmlFileName2)
            except:
                # print( "get tree paths error in " + xmlFileName2)
                treePathsOfXmlFileName2 = []
            if treePathsOfXmlFileName1.__len__() == 0 or treePathsOfXmlFileName2.__len__() == 0 \
                    or (treePathsOfXmlFileName1.__len__() >= (3 * treePathsOfXmlFileName2.__len__())) \
                    or ((3 * (treePathsOfXmlFileName1.__len__())) <= treePathsOfXmlFileName2.__len__()):
                # print(xmlFileName1,xmlFileName2)
                simOfTwoXmlFile = 0
            else:
                editence = dtwAcs.DTW_ACS(
                    ACS.getSimilarityByAcs(treePathsOfXmlFileName1, treePathsOfXmlFileName2))  # 树的距离
                simOfTwoXmlFile = (max(treePathsOfXmlFileName1.__len__(),
                                       treePathsOfXmlFileName2.__len__()) - editence) / max(
                    treePathsOfXmlFileName1.__len__(), treePathsOfXmlFileName2.__len__())  # xml文件树的相似度
            if simOfTwoXmlFile >= 0.7:  # 两棵树的相似度大于0.7就认为是相似的
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
    res = apkName1 + "," + apkName2 + ":" + simRes
    if float(simRes) >= 0.72:
        writeToTxt(res, APPSimText)  # 将相似性写入文件
    writeToTxt(res, scoreTxt)  # 将相似性写入文件

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
    AppSimFile = r'E:\APKDataSet\XiaoMiResults\MyMethods\Original\6\AppSim.txt'
    file_path = r'E:\APKDataSet\xiaomiAPK\DecompileAPK\6'
    scoreTxt = r'E:\APKDataSet\XiaoMiResults\MyMethods\Final\6\scoreTxt.txt'  # 相似性得分
    SimTxt = r'E:\APKDataSet\XiaoMiResults\MyMethods\Final\6\sim.txt'   #重打包应用
    ProblemTxt = r'E:\APKDataSet\XiaoMiResults\MyMethods\Final\6\problem.txt'
    StaticUISimilarityCompareByXMLTree(AppSimFile,file_path,scoreTxt,SimTxt,ProblemTxt)