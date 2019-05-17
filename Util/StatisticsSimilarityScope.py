#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: ImgSimilarityCompareByHash.py
@time: 2018/12/29/029 14:26
@desc: 计算APP应用的资源哈希值
'''
#数量区间统计
def ImangeNumStatistics(file_name):
    f = open(file_name)
    DHashVal1 = f.readlines()
    total = DHashVal1.__len__()
    num_0_3 = 0
    num_3_7 = 0
    num_7_10 = 0
    for val in DHashVal1:
        num = float(val.split(' ')[-1])
        if num<= 0.3:
            num_0_3 = num_0_3 +1
        elif num >0.3 and num <= 0.7:
            num_3_7 = num_3_7 + 1
        else:
            num_7_10 = num_7_10 + 1
    print(num_0_3 / total)
    print(num_3_7 / total)
    print(num_7_10 / total)
    # print(num_0_3 / (3212+3369))
    # print(num_3_7 / (3212+3369))
    # print(num_7_10 / (3212+3369))
    print(num_0_3)
    print(num_3_7)
    print(num_7_10)



if __name__ == '__main__':
    FileName =  r'C:\Users\Song\Desktop\Data\TrainData\AppNotSimValue.txt'
    ImangeNumStatistics(FileName)
