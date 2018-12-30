#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: ImgSimilarityCompareByHash.py
@time: 2018/12/29/029 14:26
@desc: 通过DHash算法来比较两个应用之间的资源的相似性
'''
import os
import imagehash
from PIL import Image
import math
import datetime

#比较资源哈希的值的汉明距离
def compareImgSimilarity():
    file_path = file_path = r'C:\Users\Administrator\Desktop\AppXml\APKDataSet'
    file_path_lists = os.listdir(file_path)
    for path in file_path_lists:
        SimRes = 0
        dist = 32
        paths = file_path + '\\' + path
        apk_lists =  os.listdir(paths)
        fileName1 = paths + '\\' + apk_lists[0] + '\\' + 'DhashVal.txt'
        f = open(fileName1)
        DHashVal1 = f.readlines();
        fileName2 = paths + '\\' + apk_lists[1] + '\\' + 'DhashVal.txt'
        f = open(fileName2)
        DHashVal2 = f.readlines();
        for hashVal1 in DHashVal1:
            hashVal1.strip('\n')
            for hashVal2 in DHashVal2:
                hashVal2.strip('\n')
                dist = min(hamming_distance_with_hash(hashVal1,hashVal2), dist)
            if dist <= 5:
                SimRes = SimRes + 1;

        SimRes = SimRes / DHashVal1.__len__()
        print(path,SimRes)
    # return SimRes

#将资源文件的感知哈希写入文件
def SaveDHashValueToTxt():
    # file_path = r'G:\GraduationProject\APKDataSet'
    file_path = r'C:\Users\Administrator\Desktop\AppXml\APKDataSet'
    file_path_lists = os.listdir(file_path)

    for path in file_path_lists:
        paths = file_path + '\\' + path
        apk_lists =  os.listdir(paths)

        file_path1 = paths + '\\' + apk_lists[0] + '\\' + 'res'
        file_path2 = paths + '\\' + apk_lists[1] + '\\' + 'res'
        getALLImageDHash(file_path1)
        getALLImageDHash(file_path2)

#计算image的差异值哈希并写入文件
def getALLImageDHash(file_path):
    DhashValTxt = file_path.replace('res', 'DhashVal.txt')
    if os.path.exists(DhashValTxt):
        os.remove(DhashValTxt)
    for path, dir, fileList in os.walk(file_path):
        for fileName in  fileList:
            if fileName.endswith('jpg') or fileName.endswith('.png'):
                fileName = path + '\\' + fileName
                if os.path.getsize(fileName) > 800:
                    img = Image.open(fileName)
                    dhashVal = imagehash.dhash(img);
                    dhashVal = str(dhashVal)
                    writeToTxt(dhashVal,DhashValTxt)

def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

#hash值之间的汉明距离
def hamming_distance_with_hash(dhash1, dhash2):
    difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
    return bin(difference).count("1")

if __name__ == '__main__':
    startTime = datetime.datetime.now()
    SaveDHashValueToTxt()
    compareImgSimilarity()
    endTime = datetime.datetime.now()
    print((endTime - startTime).seconds)






