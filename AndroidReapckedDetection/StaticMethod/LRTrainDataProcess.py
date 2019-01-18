#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: LRTrainDataProcess.py
@time: 2019/1/18 10:59
@desc:逻辑回归训练数据的生成和处理
'''

def trainDataProcess(fileName,outFileName):
    fileName = r'C:\Users\Song\Desktop\val2\AppSimValue.txt'
    outFileName = r'C:\Users\Song\Desktop\val2\AppSimValueNew.txt'
    f = open(fileName)
    valList = f.readlines()
    f.close()
    for val in valList:
        val = val.strip('\n')
        strList = val.split(' ')
        if strList[strList.__len__() - 1] != 'none' and strList[strList.__len__() - 2] != 'none':
            val = strList[strList.__len__() - 2] + ' '+ strList[strList.__len__() - 1] + ' ' + '0'
            writeToTxt(val,outFileName)


def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close