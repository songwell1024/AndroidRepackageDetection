#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: AKAZE.py
@time: 2018/12/28/028 16:29
@desc:
'''

import numpy as np
import cv2
from matplotlib import pyplot as plt

def AKAZE():
    im1 = cv2.imread(r'C:\Users\Administrator\Desktop\AppXml\19.png')
    im2 = cv2.imread(r'C:\Users\Administrator\Desktop\AppXml\20.png')


    # load the image and convert it to grayscale
    # im1 = cv2.imread(img1)
    # im2 = cv2.imread(img2)
    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

    # initialize the AKAZE descriptor, then detect keypoints and extract
    # local invariant descriptors from the image
    # detector = cv2.AKAZE_create(threshold = 16)
    detector = cv2.AKAZE_create()
    (kps1, descs1) = detector.detectAndCompute(gray1, None)
    (kps2, descs2) = detector.detectAndCompute(gray2, None)

    print("keypoints: {}, descriptors: {}".format(len(kps1), descs1.shape))
    print("keypoints: {}, descriptors: {}".format(len(kps2), descs2.shape))

    # Match the features
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(descs1, descs2, k=2)  # typo fixed

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.8 * n.distance:
            good.append([m])

    # cv2.drawMatchesKnn expects list of lists as matches.
    im3 = cv2.drawMatchesKnn(im1, kps1, im2, kps2, good, None, flags=2)
    plt.imshow(im3)
    plt.show()
    print(len(good)/len(matches))