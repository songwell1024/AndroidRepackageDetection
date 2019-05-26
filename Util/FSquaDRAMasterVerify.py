# -*- coding: utf-8 -*-
#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: AppStaticSimlarity.py
@time: 2019/5/26/002 10:37
@desc:  验证小米市场里面的应用
'''

import os

jarPath = r"C:\Users\sp\Downloads\FSquaDRA-master\out\artifacts\FSquaDRA_master_jar\FSquaDRA-master.jar "

ignoring = open(r"C:\Users\sp\Desktop\cmp\FSquaDRA\ignoring.txt", "a")
result = open(r"C:\Users\sp\Desktop\cmp\FSquaDRA\result.txt", "a")

fileName = r'C:\Users\sp\Desktop\test\AppSim.txt'   #读取相似APK的文件
f = open(fileName,encoding='UTF-8-sig')
apkList = f.readlines()

apkDirs = r'E:\APKDownLoad\normal\22222' #APK的存放位置

resultFile = r'C:\Users\sp\Desktop\test\result\tmp.txt'


for line in apkList:
	apkHelp = line.split(':')[0]
	apk = apkHelp.split(',')
	apkName1 = apk[0]
	apkName2 = apk[1]

	try:
		apkPath1 = apkDirs + "\\" + apkName1 +".apk" +" "
		apkPath2 = apkDirs + "\\" + apkName2 +".apk" + " "
		resultPath = r"-o=" +resultFile
		command = r"java -jar " + jarPath + apkPath1 + apkPath2 + resultPath
		f = os.popen(command, "r")
		d = f.read()
		cmdList = d.split("\n")
		if cmdList[cmdList.index("Skipped files:") + 1] == apkName1:
			ignoring.write(apkName1 + "\n")
		cmdList.reverse()
		if cmdList[cmdList.index("Skipped files:") - 1] == apkName2:
			# myList.remove(apkName2)
			ignoring.write(apkName2 + "\n")
		tmp = open(resultFile, encoding='UTF-8-sig')
		if tmp != "\n":
			APKSimStr = tmp.read()
			APKSimStr = APKSimStr.strip('\n')
			if APKSimStr.split(',')[-1] == 'same':
				result.write(APKSimStr + '\n')
		tmp.close()
	except:
		print(apkName1 + " " + apkName2)
ignoring.close()
result.close()
