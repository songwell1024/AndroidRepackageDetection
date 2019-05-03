#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: GetTreePath.py
@time: 2018/12/20/020 16:17
@desc:获取树的路径
获取的是静态的页面
'''


import StaticUICompareByXMLTree.GetTreePath as GTP


if __name__ == '__main__':
    filename = r'C:\Users\Song\Desktop\AppXml\c1\com.mydream.wifi.fromXiaomi\activity_bluetooth.xml'
    print(GTP.getAllSubPathOfTree(filename))