#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: AppStaticSimlarity.py
@time: 2019/1/2/002 10:37
@desc:  APP的静态相似性
'''
import StaticMethod.ImageHashSimilarity as IHS
import StaticMethod.CompentsAndPermissionSimilarity as CAPS
import os
import StaticMethod.CompentsAndPermission as CAP


#从文件中读取并进行相似性的比较
def readTxtToArrayAndCompareSimilarity(filePath,OutPutSimFile):
    # x = 1;
    # y = 1;
    # if os.path.exists(OutPutSimFile):
    #     os.remove(OutPutSimFile)
    file_path_lists = os.listdir(filePath)

    list_length = file_path_lists.__len__()
    for i in range(list_length):
        imgHash_fileName1 = filePath + '\\' + file_path_lists[i] + '\\' +'DhashVal.txt'
        CP_fileName1 = filePath + '\\' + file_path_lists[i] + '\\' + 'AndroidManifest.xml'
        try:
            DHashVal1 = readDashVal(imgHash_fileName1)
        except:
            print(imgHash_fileName1)
        try:
            dict1 = ReadAndroidManifest(CP_fileName1)
        except:
            print(CP_fileName1)
        for j in range(i + 1, list_length):

            #图片资源相似性
            imgHash_fileName2 = filePath + '\\' + file_path_lists[j] + '\\' +'DhashVal.txt'
            try:
                DHashVal2 = readDashVal(imgHash_fileName2)
                imgHashSimVal = IHS.compareImgSimilarity(DHashVal1, DHashVal2)
            except:
                print("compare image similarity error in readTxtToArrayAndCompareSimilarity: " + imgHash_fileName2)
                imgHashSimVal = 0
            #组件和权限相似性
            CP_fileName2 = filePath + '\\' + file_path_lists[j] + '\\' +'AndroidManifest.xml'
            try:
                dict2 = ReadAndroidManifest(CP_fileName2)
                CPSimVal = CAPS.compareSimilarityByComponentsAndPermission(dict1, dict2);
            except:
                print("compare similarity by components and permission error in readTxtToArrayAndCompareSimilarity : " + CP_fileName2)
                CPSimVal = 0
            try:
                if (float(imgHashSimVal) * 0.39 + float(CPSimVal) *0.61) >= 0.49:
                    simVal = file_path_lists[i] + ',' + file_path_lists[j] + ': ' + str(imgHashSimVal) + ' ' + str(CPSimVal) + " " + str(float(imgHashSimVal) * 0.39 + float(CPSimVal) *0.61)
                    writeToTxt(simVal, OutPutSimFile)
            except:
                print("Compare error in: " + file_path_lists[i] + ',' + file_path_lists[j])
            # simVal = file_path_lists[i] + ', ' + file_path_lists[j]+ ': ' + imgHashSimVal + ' ' + str(CPSimVal)

            # if x <= 2000000:
            #     OutPutSimFile = r'C:\Users\Song\Desktop\AppSimTxt' + '\\' + str(y) + ".txt"
            #     writeToTxt(simVal,OutPutSimFile)
            #     x = x + 1
            # else:
            #     y = y + 1
            #     OutPutSimFile = r'C:\Users\Song\Desktop\AppSimTxt' + '\\' + str(y) + ".txt"
            #     writeToTxt(simVal, OutPutSimFile)
            #     x = 1;


def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

def readDashVal(fileName1):
    DHashVal1 = []
    if os.path.exists(fileName1):
        f = open(fileName1)
        DHashVal1 = f.readlines()
        f.close()
    else:
        print("There is no such file--" + fileName1)  # 看下出问题的文件夹
    return DHashVal1

def ReadAndroidManifest(fileName1):
    dict1 = {}

    if os.path.exists(fileName1):
       dict1 = CAP.getElementFrequency(fileName1)
    else:
        print("There is no such file--" + fileName1)
    return dict1