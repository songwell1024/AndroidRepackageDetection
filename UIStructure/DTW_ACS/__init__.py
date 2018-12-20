#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/12/20/020 16:02
@desc: ACS所有公共子序列
DTW：动态时间归整
该算法是用来比较树的相似度的
'''

import DTW_ACS.GetTreePath as GTP


if __name__ == '__main__' :
    file_name = r'C:\Users\Administrator\Desktop\AndroidManifestTxt\demo.xml'
    print(GTP.getXmlData(file_name))
    # print(GTP.getStrXmlMap(file_name))