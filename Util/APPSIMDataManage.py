#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/5/15/025 21:29
@desc: 功能函数，用于统计APP的大小
'''

def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close


def manageNotSimAppData(inputFileName1,inputFileName2,outFileName):
    f1 = open(inputFileName1)
    strings1 = f1.readlines()

    f2 = open(inputFileName2)
    strings2 = f2.readlines()

    dataSets = []
    for i in range(strings1.__len__()):
        ss = strings1[i].split(":")[0] + ": " + strings2[i].split(" ")[0] + " "+ strings2[i].split(" ")[1]
        writeToTxt(ss,outFileName)


if __name__ == "__main__":
    inputFileName1 = r'C:\Users\Song\Desktop\APPSIM\1.txt'
    inputFileName2 = r'C:\Users\Song\Desktop\APPSIM\AppSimValue.txt'
    outFileName = r'C:\Users\Song\Desktop\APPSIM\2.txt'
    manageNotSimAppData(inputFileName2,inputFileName1,outFileName)

