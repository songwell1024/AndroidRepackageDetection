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


#获取数量
def getImageNumberOfAPP(file_path,outFileName):
    file_path_lists = os.listdir(file_path)

    for path in file_path_lists:
        fileName = file_path + '\\' + path + '\\' + 'DhashVal.txt'
        if os.path.exists(fileName):
            f = open(fileName)
            DHashVal1 = f.readlines()
            num = DHashVal1.__len__()
            writeToTxt(path + ":" + str(num),outFileName)
        else:
            print("error: " + path)


#数量区间统计
def ImangeNumStatistics(file_name):
    f = open(file_name)
    DHashVal1 = f.readlines()
    num_100 = 0       #<100
    num_100_200 = 0     #200>num>100
    num_200_300 = 0     #300>num>200
    num_300_400 = 0     #400>num>300
    num_400_500 = 0     #500>num>400
    num_500_600 = 0     #600>num>500
    num_600_700 = 0     #700>num>600
    num_700_800 = 0     #800>num>700
    num_800_900 = 0     #900>num>800
    num_900_1000 = 0     #1000>num>900
    num_1000_0 = 0      # num>1000
    for val in DHashVal1:
        num = val.split(':')[1]
        if num<= 100:
            num_100 = num_100 +1;
        elif num >100 and num <= 200:
            num_100_200 = num_100_200 + 1
        elif num >200 and num <= 300:
            num_200_300 = num_200_300 + 1
        elif num >300 and num <= 400:
            num_300_400 = num_300_400 + 1
        elif num >400 and num <= 500:
            num_400_500 = num_400_500 + 1
        elif num >500 and num <= 600:
            num_500_600 = num_500_600 + 1
        elif num >600 and num <= 700:
            num_600_700 = num_600_700 + 1
        elif num >700 and num <= 800:
            num_700_800 = num_700_800 + 1
        elif num >800 and num <= 900:
            num_800_900 = num_800_900 + 1
        elif num >900 and num <= 1000:
            num_900_1000 = num_900_1000 + 1
        else:
            num_1000_0 = num_1000_0 + 1

def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close


if __name__ == '__main__':
    file_path = r'C:\Users\Song\Desktop\APPPath\c1'
    outFileName = r'C:\Users\Song\Desktop\APPVal\imageNum.txt'
    getImageNumberOfAPP(file_path,outFileName)