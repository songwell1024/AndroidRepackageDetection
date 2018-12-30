#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/12/28/028 21:45
@desc:  爬取AndroZoo公开的重打包数据集
'''

import os,shutil
import urllib
import requests

def Androzoo():
    index = 0
    f = open(r'C:\Users\Administrator\Desktop\AppXml\app.txt')
    contents = f.readlines()
    for content in contents:
        strs = content.split(',')
        fpath = r'G:\GraduationProject\APKDataSet' + '\\' + str(index)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        file_name = fpath + '\\' + strs[0] + '.apk'
        url = r'https://androzoo.uni.lu/api/download?apikey=62ab45d52429ca7d890b81343b310061a29efe7dff1e4aa9e5507905c62c0315&sha256=' + strs[0]
        urllib.request.urlretrieve(url, file_name)
        file_name = fpath + '\\' + strs[1].strip('\n') + '.apk'
        url = r'https://androzoo.uni.lu/api/download?apikey=62ab45d52429ca7d890b81343b310061a29efe7dff1e4aa9e5507905c62c0315&sha256=' + strs[1]
        urllib.request.urlretrieve(url, file_name)
        index = index + 1
    print("The spider completed")

if __name__ == '__main__':
    # Androzoo()
    print("complete")