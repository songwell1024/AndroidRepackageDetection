#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/12/25/025 21:29
@desc:
'''
import StaticMethod.DataProcessAndShow as DPAS
import StaticMethod.CalculateImageHash as CIH
import StaticMethod.AppStaticSimlarity as ASS


def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

if __name__ == '__main__' :


    # ApkFilePath = r'C:\Users\Song\Desktop\aaaa'  # 数据集文件
    # # OutPutSimFile = r'C:\Users\Song\Desktop\AppSimTxt\AppSimValue.txt'  # APP的相似性文件
    # startTime = datetime.datetime.now()
    # CIH.SavePHashValueToTxt(ApkFilePath)   #计算感知哈希
    # # ASS.readTxtToArrayAndCompareSimilarity(ApkFilePath, OutPutSimFile)  #相似性比较
    # ASS.readTxtToArrayAndCompareSimilarity(ApkFilePath)  #相似性比较
    # endTime = datetime.datetime.now()
    # print('执行时间： ' + str((endTime - startTime)) + 's')

    #数据的展示
    fileName1 = r'C:\Users\Song\Desktop\Data\TrainData\AppSimValue.txt'
    fileName2 = r'C:\Users\Song\Desktop\Data\TrainData\AppNotSimValue.txt'
    DPAS.dataPeocessAndShow(fileName1,fileName2)