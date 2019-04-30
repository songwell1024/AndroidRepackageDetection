#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/12/20/020 16:02
@desc:
ACS: 所有公共子序列
DTW：动态时间归整
该算法是用来比较树的相似度的
'''

import DynamicMethod.DTW_ACS.ACS as ACS
import DynamicMethod.DTW_ACS.dtwAcs as dtwAcs

# import XMLTree.EditDistance as ED

from PIL import Image

if __name__ == '__main__' :
    # file_name = r'C:\Users\Administrator\Desktop\AndroidManifestTxt\demo.xml'
    #
    #
    # print(GTP.getAllSubPathOfTree(file_name))
    print("aaa")
    # print(GTP.getAllSubPathOfTree(file_name))
    # print(GTP.getAllSubPathOfTree(file_name))

    # str_array = ['a','b','b','c','r','s','b']
    # print(L(str_array,'c',6))
    # ACS.getNumberOfCommonDistinctSubsequences()
    # print(GTP.getStrXmlMap(file_name))



    s = [['a','b'],['a','d','c'],['a','d','d'],['a','c']]
    t = [['a','b'],['a','c','d'],['a','c','c'],['a','d']]
    #
    # ss = [['a', 'b'], ['a', 'b', 'c'], ['a', 'b', 'd', 'e']]
    # tt = [['a', 'b','b'], ['a', 'b', 'c','d','e']]
    #
    # sss = [['a', 'b','c'], ['a', 'd', 'e'], ['a', 'g', 'd']]
    # ttt = [['a', 'b', 'c','d'], ['a', 'd', 'e','f'], ['a', 'g', 'd','m']]
    #
    # ssss = [['a', 'b', 'c'], ['a', 'd', 'e'], ['a', 'g', 'd']]
    # tttt = [['a', 'b', 'c'], ['a', 'd', 'e','f'], ['a', 'g', 'd', 'm']]
    #
    # sssss = [['a', 'b', 'c'], ['a', 'd', 'e'], ['a', 'g', 'd']]
    # ttttt = [['a', 'b', 'c'], ['a', 'd', 'e'], ['a', 'g', 'd', 'm'],['a', 'b', 'c']]
    #
    # ssssss = [['a', 'b', 'c'], ['a', 'd', 'e'], ['a', 'g', 'd']]
    # tttttt = [['a', 'b', 'g', 'b'], ['a', 'd', 'd','f'], ['a', 'c', 'e']]
    #
    #
    # sssssss = [['c', 'e'], ['c', 'p'], ['c', 'k'],['c','b','b','d'],['c','b','b','d','a']]
    # ttttttt = [['c', 'e', 'p'], ['c', 'e', 'k'], ['c', 'e', 'b','b','d'], ['c','e','b','b', 'a'],['c','e']]
    # # print(ACS.getSimilarityByAcs(ss,tt))
    print(dtwAcs.DTW_ACS(ACS.getSimilarityByAcs(s, t)))
    # print(dtwAcs.DTW_ACS(ACS.getSimilarityByAcs(ss,tt)))
    # print(dtwAcs.DTW_ACS(ACS.getSimilarityByAcs(sss, ttt)))
    # print(dtwAcs.DTW_ACS(ACS.getSimilarityByAcs(ssss,tttt)))
    # print(dtwAcs.DTW_ACS(ACS.getSimilarityByAcs(sssss, ttttt)))
    # print(dtwAcs.DTW_ACS(ACS.getSimilarityByAcs(ssssss, tttttt)))
    # print(dtwAcs.DTW_ACS(ACS.getSimilarityByAcs(sssssss, ttttttt)))
    #
    # print("===============================================")
    # s1 = "abddccd"
    # t1 = "abccddc"
    #
    # ss1 = 'abbbcde'
    # tt1 = 'abbbcde'
    #
    # sss1 = 'abdgced'
    # ttt1 = 'abdgcedfm'
    #
    # ssss1 = 'abdgced'
    # tttt1 = 'abdgcedm'
    #
    # sssss1 =  'abdgced'
    # ttttt1 =  'abdgbcedcm'
    #
    # ssssss1 = 'abdgced'
    # tttttt1 = 'abdcgdedf'
    #
    # sssssss1 = 'cepkbebda'
    # ttttttt1 = 'ceepkbbda'
    #
    # print(ED.editDistanceSimilarity(s1,t1))
    # print(ED.editDistanceSimilarity(ss1, tt1))
    # print(ED.editDistanceSimilarity(sss1, ttt1))
    # print(ED.editDistanceSimilarity(ssss1, tttt1))
    # print(ED.editDistanceSimilarity(sssss1, ttttt1))
    # print(ED.editDistanceSimilarity(ssssss1, tttttt1))
    # print(ED.editDistanceSimilarity(sssssss1, ttttttt1))
    #
    # print("===============================================")
    # s11 = "a(b,d(c),d(d),c)"
    # t11 = "a(b,c(d),c(c),d)"
    #
    ss11 = 'a(b,b(c),b(d(e)))'
    tt11 = 'a(b(b),b(c(d(e))))'
    #
    # sss11 = 'a(b(c),d(e),g(d))'
    # ttt11 = 'a(b(c),d(e(f)),g(d(m)))'
    #
    # ssss11 = 'a(b(c),d(e),g(d))'
    # tttt11 = 'a(b(c),d(e),g(d(m)))'
    #
    # sssss11 = 'a(b(c),d(e),g(d))'
    # ttttt11 = 'a(b(c),d(e),g(d(m)),b(c))'
    #
    # ssssss11 = 'a(b(c),d(e),g(d))'
    # tttttt11 = 'a(b(g(d)),d(d(f)),c(e))'
    #
    sssssss11 = 'c(e, p, k, b(b(d, a)), e)'
    ttttttt11 = 'c(e(p, k, b(b(d, a))),e)'
    #
    # print(ED.editDistanceSimilarity(s11, t11))
    # print(ED.editDistanceSimilarity(ss11, tt11))
    # print(ED.editDistanceSimilarity(sss11, ttt11))
    # print(ED.editDistanceSimilarity(ssss11, tttt11))
    # print(ED.editDistanceSimilarity(sssss11, ttttt11))
    # print(ED.editDistanceSimilarity(ssssss11, tttttt11))
    # print(ED.editDistanceSimilarity(sssssss11, ttttttt11))
    #
    # print("===============================================")
    # s111 = "a1(b2,d2(c3),d1(d3),c2)"
    # t111 = "a1(b2,c2(d3),c2(c3),d2)"
    #
    # ss111 = 'a1(b2,b2(c3),b2(d3(e4)))'
    # tt111 = 'a1(b2(b3),b2(c3(d4(e5))))'
    #
    # sss111 = 'a1(b2(c3),d2(e3),g2(d3))'
    # ttt111 = 'a1(b2(c3),d2(e3(f4)),g2(d3(m4)))'
    #
    # ssss111 = 'a1(b2(c3),d2(e3),g2(d3))'
    # tttt111 = 'a1(b2(c3),d2(e3),g2(d3(m4)))'
    #
    # sssss111 = 'a1(b2(c3),d2(e3),g2(d3))'
    # ttttt111 = 'a1(b2(c3),d2(e3),g2(d3(m4)),b2(c3))'
    #
    # ssssss111 = 'a1(b2(c3),d2(e3),g2(d3))'
    # tttttt111 = 'a1(b2(g3(d4)),d2(d3(f4)),c2(e3))'
    #
    sssssss111 = 'c1(e2, p2, k2, b2(b3(d4, a4)), e2)'
    ttttttt111 = 'c1(e2(p3, k3, b3(b4(d5, a5))), e2)'
    #
    # print(ED.editDistanceSimilarity(s111, t111))
    # print(ED.editDistanceSimilarity(ss111, tt111))
    # print(ED.editDistanceSimilarity(sss111, ttt111))
    # print(ED.editDistanceSimilarity(ssss111, tttt111))
    # print(ED.editDistanceSimilarity(sssss111, ttttt111))
    # print(ED.editDistanceSimilarity(ssssss111, tttttt111))
    # print(ED.editDistanceSimilarity(sssssss111, ttttttt111))

