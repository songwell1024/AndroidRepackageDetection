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
    im1 = Image.open(r'C:\Users\Administrator\Desktop\AppXml\7.png')
    # im2 = Image.open(r'C:\Users\Administrator\Desktop\AppXml\6.png')
    im2 = Image.open(r'C:\Users\Administrator\Desktop\AppXml\8.png')
    dhash1 = imagehash.dhash(im1);
    dhash2  = imagehash.dhash(im2);
    print(dhash1,dhash2)
    # difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
    # print(bin(difference).count("1"))
    # # im3 = Image.open(r'C:\Users\Administrator\Desktop\AppXml\3.png')
    print(DHash.hamming_distance(im1,im2))
    print(DHash.calculate_hash(im2))

    print(os.path.getsize(r'C:\Users\Administrator\Desktop\AppXml\7.png'))