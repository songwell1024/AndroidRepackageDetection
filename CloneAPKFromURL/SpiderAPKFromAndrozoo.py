#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: SpiderAPKFromAndrozoo.py.py
@time: 2018/12/28/028 21:45
@desc:  爬取AndroZoo公开的重打包数据集
'''

import os
import urllib
import time

def Androzoo():
    index = 2451
    f = open(r'C:\Users\Administrator\Desktop\AppXml\app.txt')
    contents = f.readlines()
    j = contents.__len__()
    i = 0
    while(j > 0):
        strs = contents[i].strip('\n')
        fpath = r'E:\GraduationProject\APKDataSetNotSimilar' + '\\' + str(index)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        file_name = fpath + '\\' + strs + '.apk'
        url = r'https://androzoo.uni.lu/api/download?apikey=62ab45d52429ca7d890b81343b310061a29efe7dff1e4aa9e5507905c62c0315&sha256=' + strs
        try:
            urllib.request.urlretrieve(url, file_name)
        except:
            print("continue")
            time.sleep(10)
        time.sleep(3)
        i = i + 1
        j = j - 1
        strs = contents[i].strip('\n')
        file_name = fpath + '\\' + strs + '.apk'
        url = r'https://androzoo.uni.lu/api/download?apikey=62ab45d52429ca7d890b81343b310061a29efe7dff1e4aa9e5507905c62c0315&sha256=' + strs
        try:
            urllib.request.urlretrieve(url, file_name)
        except:
            print("continue")
            time.sleep(10)
        time.sleep(4)
        index = index + 1
        i = i + 1
        j = j - 1
    print("The spider completed")

if __name__ == '__main__':
    Androzoo()
    print("complete")