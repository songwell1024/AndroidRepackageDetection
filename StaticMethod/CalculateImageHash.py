#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: ImgSimilarityCompareByHash.py
@time: 2018/12/29/029 14:26
@desc: 计算APP应用的资源哈希值
'''
import os
import imagehash
from PIL import Image

#将资源文件的感知哈希写入文件
def SavePHashValueToTxt(file_path):
    file_path_lists = os.listdir(file_path)

    for path in file_path_lists:
        app_path = file_path + '\\' + path + '\\' + 'res'
        getALLImageDHash(app_path)
        # try:
        #     getALLImageDHash(app_path)
        # except:
        #     print("calculate image hash error in CalculateImageHash: " +  app_path)

#计算image的差异值哈希并写入文件
def getALLImageDHash(file_path):
    DhashValTxt = file_path.replace('res', 'DhashVal.txt')
    if os.path.exists(DhashValTxt):
        os.remove(DhashValTxt)
    for path, dir, fileList in os.walk(file_path):
        for fileName in  fileList:
            if fileName.endswith('.jpg') or fileName.endswith('.png'):
                fileName = path + '\\' + fileName
                if os.path.getsize(fileName) > 800:
                    try:
                        img = Image.open(fileName)
                        phashVal = imagehash.phash(img)
                        phashVal = str(phashVal)
                        if phashVal != '0000000000000000':
                            writeToTxt(phashVal, DhashValTxt)
                    except:
                        print("image hash error: " + fileName)

def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close