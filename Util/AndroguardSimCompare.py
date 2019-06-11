# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: AppStaticSimlarity.py
@time: 2019/5/26/002 10:37
@desc:  androguard来验证我们的方法和FSquaDRA检测出的应用
'''
import os
from decimal import Decimal
import time
import subprocess
import psutil


PIDList = []
PIDnumber = 2

class TimeoutError(Exception):
    pass


def openCommand(cmd, timeout=1200):
    """执行命令cmd，返回命令输出的内容。
    如果超时将会抛出TimeoutError异常。
    cmd - 要执行的命令
    timeout - 最长等待时间，单位：秒
    """
    global PIDnumber
    p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
    t_beginning = time.time()
    pids = psutil.pids()
    for pid in pids:
        pp = psutil.Process(pid)
        if pp.name() == 'python.exe':
            if PIDList.__len__() > 1 and (not PIDList.__contains__(pid)):
                PIDList[1] = pid
            else:
                if not PIDList.__contains__(pid):
                    PIDList.append(pid)
    seconds_passed = 0
    while True:
        if p.poll() is not None:
            break
        seconds_passed = time.time() - t_beginning
        if timeout and seconds_passed > timeout:
            p.terminate() #只能杀死终端进程，其打开的子进程不能终止
            p.kill()
            if PIDList.__len__() >= 1:
                cmdStr = r'taskkill /pid ' + str(PIDList[1]) + ' /F'
                os.system(cmdStr)
            # os.killpg(os.getpgid(p.pid), 9)  #终止该终端创建的所有子进程.linux下有效
            raise TimeoutError(cmd, timeout)
        time.sleep(0.1)
    return p.stdout.readlines()


if __name__ == "__main__":

    fileName = r'E:\APKDataSet\WanDouJiaResults\MyMethods\Final\3\sim1.txt'  # 读取相似APK的文件
    fileRead = open(fileName, encoding='UTF-8-sig')
    # fileRead = open(fileName)
    apkList = fileRead.readlines()

    apkDirs = r'E:\APKDataSet\wandoujiaAPK\33333'  # 安卓应用所在文件目录

    os.chdir(r'E:\APKDataSet\androguard-2.0')

    for line in apkList:
        score = open(r"E:\APKDataSet\WanDouJiaResults\Androguard\3\score.txt", "a")
        result = open(r"E:\APKDataSet\WanDouJiaResults\Androguard\3\result.txt", "a")
        apkHelp = line.split(':')[0]
        apk = apkHelp.split(',')
        apkName1 = apk[0]
        apkName2 = apk[1]

        try:
            apkPath1 = apkDirs + "\\" + apkName1 + ".apk" + " "
            apkPath2 = apkDirs + "\\" + apkName2 + ".apk"
            command = r"python androsim.py -i " + apkPath1 + apkPath2
            # f = os.popen(command, "r")
            # d = f.read()
            time.sleep(20)
            cmdList = openCommand(command, 1200)  # 20分钟无法比较完一组直接退出当前线程
            # cmdList = d.split("\n")
            try:
                for string in cmdList:
                    string = str(string)
                    if string.__contains__("methods:") and string.__contains__("similarities"):
                        strList = string.split(" ")
                        SimScore = strList[2]
                        SimScore = SimScore.replace('%', '0')
                        SimScore = float(SimScore) / 100
                        SimScore = str(float(Decimal(SimScore).quantize(Decimal('0.000'))))
                        score.write(apkName1 + "," + apkName2 + ":" + SimScore + '\n')
                        if float(SimScore) > 0.5:
                            result.write(apkName1 + "," + apkName2 + ":" + SimScore + '\n')
            except:
                CannotCompare = open(r"E:\APKDataSet\WanDouJiaResults\Androguard\3\CannotCompare.txt", "a")
                CannotCompare.write(apkName1 + "," + apkName2+"\n")
                CannotCompare.close()
        except:
            print(apkName1 + " " + apkName2)
            CannotCompare = open(r"E:\APKDataSet\WanDouJiaResults\Androguard\3\CannotCompare.txt", "a")
            CannotCompare.write(apkName1 + "," + apkName2+ "\n")
            CannotCompare.close()
        score.close()
        result.close()

########################################################################################################################
# # -*- coding: utf-8 -*-
# # -*- coding: utf-8 -*-
# #!/usr/bin/env python
# # encoding: utf-8
# '''
# @author: WilsonSong
# @license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
# @contact: songzhiqwer@gmail.com
# @software: garner
# @file: AppStaticSimlarity.py
# @time: 2019/5/26/002 10:37
# @desc:  androguard来验证我们的方法和FSquaDRA检测出的应用
# '''
# import os
#
# if __name__ == "__main__":
#
# 	fileName = r'E:\APKDataSet\WanDouJiaResults\MyMethods\Final\3\sim.txt'   #读取相似APK的文件
# 	fileRead = open(fileName,encoding='UTF-8-sig')
# 	# fileRead = open(fileName)
# 	apkList = fileRead.readlines()
#
# 	apkDirs = r'E:\APKDataSet\wandoujiaAPK\33333'    #安卓应用所在文件目录
#
# 	os.chdir(r'E:\APKDataSet\androguard-2.0')
#
# 	for line in apkList:
# 		score = open(r"E:\APKDataSet\WanDouJiaResults\Androguard\3\score.txt", "a")
# 		result = open(r"E:\APKDataSet\WanDouJiaResults\Androguard\3\result.txt", "a")
# 		apkHelp = line.split(':')[0]
# 		apk = apkHelp.split(',')
# 		apkName1 = apk[0]
# 		apkName2 = apk[1]
#
# 		try:
# 			apkPath1 = apkDirs + "\\" + apkName1 + ".apk"+ " "
# 			apkPath2 = apkDirs + "\\" + apkName2 + ".apk"
# 			command = r"python androsim.py -i "+ apkPath1 + apkPath2
# 			f = os.popen(command, "r")
# 			d = f.read()
# 			cmdList = d.split("\n")
# 			try:
# 				for string in cmdList:
# 					if string.__contains__("methods:") and string.__contains__("similarities"):
# 						strList = string.split(" ")
# 						SimScore = strList[2]
# 						score.write(apkName1 +" "+ apkName2 + " " + SimScore +'\n')
# 						SimScore = SimScore.replace('%', '0')
# 						float(SimScore)
# 						if float(SimScore) > 50:
# 							result.write(apkName1 +" "+ apkName2 +": " + SimScore +'\n')
# 			except:
# 				CannotCompare = open(r"E:\APKDataSet\WanDouJiaResults\Androguard\3\CannotCompare.txt")
# 				CannotCompare.write(apkName1 +" "+ apkName2)
# 				CannotCompare.close()
# 		except:
# 			print(apkName1 + " " + apkName2)
# 		score.close()
# 		result.close()
