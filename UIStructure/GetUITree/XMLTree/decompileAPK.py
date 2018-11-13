#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: DecompileAPK.py.py
@time: 2018/11/7/007 15:52
@desc:
'''
import datetime
import time
import subprocess
import os

def decompileAPk(apkPath,outputPath,threadNum):

    # # apkPath: apk 的存储路径
    # # outputPath:用apktool 反编译apk 之后的存储路径
    apkList = os.listdir(apkPath)
    childNum = 0
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




# 如果APK的存储目录是按照类别划分的时候
# def decompileAPk(apkPath,outputPath,threadNum):
#
#     # # apkPath: apk 的存储路径
#     # # outputPath:用apktool 反编译apk 之后的存储路径
#
#     # 由于APK的存储是按照类别来划分的，所以获取到每一个apk的存储类别
#     dirlist = os.listdir(apkPath)
#     childNum = 0
#     # 将apk 反编译之后还是将它们按照原先的类别存储
#     for i in range(len(dirlist)):  # 得到apk 文件夹下的每一个子的类别
#         filelist = apkPath + "\\" + dirlist[i]  # 获取每个类别的路径
#         apklist = os.listdir(filelist)  # 获取每个路径下的apk 列表
#         category_output = outputPath + "\\" + dirlist[i]  # 输出的路径列表
#
#         if not os.path.exists(category_output):  # 如果输出的路径不存在那么就创建一个路径
#             os.makedirs(category_output)
#
#         for APK in apklist:
#             portion = os.path.splitext(APK)  # 将apk文件按照它们的文件名和后缀做一个分割
#             apkOutpath = os.path.join(category_output, portion[0])  # portion 中 存储的是apk的文件名
#             APK = os.path.join(apkPath + "\\" + dirlist[i], APK)
#             if not os.path.exists(apkOutpath):
#                os.makedirs(apkOutpath)
#
#             APK = '"' + APK + '"'
#             apkOutpath = '"' + apkOutpath  + '"'
#             cmd = "apktool d -f {0} -o {1}".format(APK, apkOutpath)  # 反编译出来apk 之后按照文件名在存储
#             #os.system(cmd)
#             #subprocess.run(cmd, shell=True)
#             # 开启多个线程执行,
#             child = subprocess.Popen(cmd, shell=True, close_fds=True)
#             childNum = childNum + 1
#             print("A APk is decompiling")
#             if childNum == threadNum:
#                 child.wait()
#                 childNum = 0
#     while child.poll() is None:
#         print("please wait~")
#         time.sleep(10)
#     print("All work done! Happy everyday~")


# def timeout_command(command, timeout):
#     start = datetime.datetime.now()
#     process = subprocess.Popen(command, bufsize=10000, stdout=subprocess.PIPE, close_fds=True)
#     while process.poll() is None:
#         time.sleep(0.1)
#         now = datetime.datetime.now()
#         if (now - start).seconds > timeout:
#             try:
#                 process.terminate()
#             except Exception as e:
#                 return None
#             return None
#     out = process.communicate()[0]
#     if process.stdin:
#         process.stdin.close()
#     if process.stdout:
#         process.stdout.close()
#     if process.stderr:
#         process.stderr.close()
#     try:
#         process.kill()
#     except OSError:
#         pass
#     return out
