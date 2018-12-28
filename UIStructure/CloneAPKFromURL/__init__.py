#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/12/28/028 21:45
@desc:
'''

import os,shutil
import urllib
import requests

def mymovefile(srcfile,fpath):

    if not os.path.exists(fpath):
        os.makedirs(fpath)                #创建路径
    shutil.move(srcfile,dstfile)          #移动文件

if __name__ == '__main__':
    index = 0
    f = open(r'C:\Users\Administrator\Desktop\AppXml\app.txt')
    contents = f.readlines()
    for content in contents:
        str = content.split(',')


    fpath = r'C:\Users\Administrator\Desktop\AppXml'
    os.makedirs(fpath)
    url = r'https://androzoo.uni.lu/api/download?apikey=62ab45d52429ca7d890b81343b310061a29efe7dff1e4aa9e5507905c62c0315&sha256=054D2F61D64389E0073CDF1948EF84B2532CEC807B3286D7257C9A8D1674A6C5'
    urllib.request.urlretrieve(url, file_path)
