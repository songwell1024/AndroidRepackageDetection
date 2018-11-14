#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: init_demo.py
@time: 2018/11/14/014 9:29
@desc: 测试主函数
'''

import AndroidManifestInformation.ProcessAndroidManifest as PAM
import XMLTree.DecompileAPK as DeAPK
import os
import numpy



def writeToTxt(str,fileName):
    f = open(fileName, 'a')
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

if __name__ == '__main__':
    # # # ApkPath = r'C:\Users\Administrator\Desktop\qqq'  # APK文件的路径
    # ApkDecompileOutputPath = r'C:\Users\Administrator\Desktop\decompile'  # 反编译文件的输出路径
    # # #
    # # # # DeAPK.decompileAPk(ApkPath, ApkDecompileOutputPath, 10)  # 反编译APK文件
    # PAM.getElementFrequency(ApkDecompileOutputPath)
    PAM.readTxtToArrayAndCompareSimilarity(r'C:\Users\Administrator\Desktop\AndroidManifestTxt\AndroidManifestTxt.txt')
