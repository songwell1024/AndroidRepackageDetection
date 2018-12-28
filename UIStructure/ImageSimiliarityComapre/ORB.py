#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: ORB.py
@time: 2018/12/28/028 14:26
@desc:
'''
import numpy as np
import cv2
from matplotlib import pyplot as plt

def ORB():

    img1 = cv2.imread(r'C:\Users\Administrator\Desktop\AppXml\19.png')
    img2 = cv2.imread(r'C:\Users\Administrator\Desktop\AppXml\22.png')

    # 最大特征点数,需要修改，5000太大。
    orb = cv2.ORB_create(100)

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # img1 = cv2.drawKeypoints(img1, kp1, img1)
    # img2 = cv2.drawKeypoints(img2, kp2, img2)

    #
    # cv2.imshow('sp', img1)
    # cv2.imshow('sp', img2)
    # cv2.imwrite('imgpng', img2)
    # cv2.waitKey(1000)
    # cv2.destroyAllWindows()


    # # 提取并计算特征点

    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    # knn筛选结果
    matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)
    good = [m for (m, n) in matches if m.distance < 0.80 * n.distance]
    # # 查看最大匹配点数目
    print(len(good)/100)

    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches,img2, flags=2)
    # cv2.imshow('sp', img3)
    # cv2.waitKey(0)
    plt.imshow(img3), plt.show()