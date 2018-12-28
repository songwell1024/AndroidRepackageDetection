#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: surf.py
@time: 2018/12/26/026 17:01
@desc:
'''


import cv2

# img1 = cv2.imread(r'C:\Users\Administrator\Desktop\AppXml\1.png')
    # img2 = cv2.imread(r'C:\Users\Administrator\Desktop\AppXml\8.png')
    #
    # # 参数为hessian矩阵的阈值
    # surf = cv2.xfeatures2d.SURF_create(2000)
    #
    # # 设置是否要检测方向
    # surf.setUpright(True)
    #
    # # # 输出设置值
    # # print(surf.getUpright())
    #
    # # 找到关键点和描述符
    # key_query1, desc_query1 = surf.detectAndCompute(img1, None)
    # key_query2, desc_query2 = surf.detectAndCompute(img2, None)
    #
    # img1 = cv2.drawKeypoints(img1, key_query1, img1)
    # img2 = cv2.drawKeypoints(img2, key_query2, img2)
    #
    # # # 输出描述符的个数
    # # print(surf.descriptorSize())
    # cv2.imshow('sp', img1)
    # cv2.imshow('sp', img2)
    # cv2.waitKey(0)