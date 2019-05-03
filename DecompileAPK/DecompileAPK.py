#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: DecompileAPk.py
@time: 2018/12/30/030 9:56
@desc: 批量反编译
'''

import time
import subprocess
import os

def decompileAPk(apkPath,outputPath,threadNum):

    # # apkPath: apk 的存储路径
    # # outputPath:用apktool 反编译apk 之后的存储路径
    apkList = os.listdir(apkPath)
    childNum = 0
    if apkList.__len__() >0:
        for APK in apkList:
            portion = os.path.splitext(APK)  # 将apk文件按照它们的文件名和后缀做一个分割
            apkOutPath = os.path.join(outputPath, portion[0])  # portion 中 存储的是apk的文件名
            APK = os.path.join(apkPath , APK)
            if not os.path.exists(apkOutPath):
               os.makedirs(apkOutPath)

            APK = '"' + APK + '"'
            apkOutPath = '"' + apkOutPath  + '"'
            cmd = "apktool d -f {0} -o {1}".format(APK, apkOutPath)  # 反编译出来apk 之后按照文件名在存储
            #os.system(cmd)
            #subprocess.run(cmd, shell=True)
            # 开启多个线程执行,
            child = subprocess.Popen(cmd, shell=True, close_fds=True)
            childNum = childNum + 1
            print("A APk is decompiling")
            if childNum == threadNum:
                child.wait()
                childNum = 0
        while child.poll() is None:
            print("please wait~")
            time.sleep(10)
    print("All work done! Happy everyday~")

if __name__ == '__main__':
    APKOutPath = r'C:\Users\Administrator\Desktop\DecompileAPKFile'
    file_path = file_path = r'C:\Users\Administrator\Desktop\DataSet'
    file_path_lists = os.listdir(file_path)
    for path in file_path_lists:
        outPath = APKOutPath + '\\' + path
        path = file_path + '\\' + path
        decompileAPk(path, outPath, 2)
