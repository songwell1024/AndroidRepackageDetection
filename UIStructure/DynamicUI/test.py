#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: test.py
@time: 2018/12/5/005 14:20
@desc:
'''

def getNum(m):
    data = ['[0,712][168,240]','[0,722][168,240]','[0,72][168,240]']
    if data.__contains__('[0,72][168,240]'):
        data.remove('[0,72][168,240]')
    print(data)

