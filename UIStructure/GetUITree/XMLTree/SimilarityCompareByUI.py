#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: SimilarityCompareByUI.py
@time: 2018/11/13/013 16:49
@desc:
'''

def SimilarityCompare(filePath):
    dirList = os.listdir(filePath)
    for i in range(len(dirList)):
        fileList = os.listdir(filePath + "\\" + dirList[i])
        fileName1 = filePath + "\\" + dirList[i] + "\\" + fileList[0]
        fileName2 = filePath + "\\" + dirList[i] + "\\" + fileList[1]



if __name__ == "__main__":
    SimilarityCompare(r'C:\Users\Administrator\Desktop\ApkOutputTxt')

