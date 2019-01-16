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
import AndroidManifestInformation.CompentsAndPermission as CAP
import XMLTree.DecompileAPK as DeAPK
import os
import numpy

if __name__ == '__main__':
    # # # ApkPath = r'C:\Users\Administrator\Desktop\qqq'  # APK文件的路径
    # ApkDecompileOutputPath = r'C:\Users\Administrator\Desktop\decompile'  # 反编译文件的输出路径
    # # #
    # # # # DeAPK.decompileAPk(ApkPath, ApkDecompileOutputPath, 10)  # 反编译APK文件
    # PAM.getElementFrequency(ApkDecompileOutputPath)
    # CAP.getElementFrequency()
    # print('aaaaa')
    CAP.getElementFrequency()