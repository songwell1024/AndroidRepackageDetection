#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/12/25/025 21:29
@desc:
'''

import StaticMethod.DHash as DHash
from PIL import Image

import os
import imagehash

if __name__ == '__main__' :
    im1 = Image.open(r'C:\Users\Administrator\Desktop\AppXml\20.png')
    # im2 = Image.open(r'C:\Users\Administrator\Desktop\AppXml\6.png')
    im2 = Image.open(r'C:\Users\Administrator\Desktop\AppXml\200.png')
    dhash1 = imagehash.dhash(im1);
    dhash2  = imagehash.dhash(im2);

    dhash1 = str(dhash1)
    dhash2 = str(dhash2)
    print(dhash1,dhash2)
    print(DHash.hamming_distance_with_hash(dhash1, dhash2))

    dhash11 = DHash.calculate_hash(im1)
    dhash22 = DHash.calculate_hash(im2)
    print(dhash11,dhash22)
    print(DHash.hamming_distance(im1,im2))
    # print(os.path.getsize(r'C:\Users\Administrator\Desktop\AppXml\7.png'))
