# -*- coding: utf-8 -*-
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
@desc:  androguard来验证我们的方法和FSquaDRA检测出的应用
'''



import os



fileName = r'C:\Users\sp\Desktop\test\AppSim.txt'   #读取相似APK的文件
f = open(fileName,encoding='UTF-8-sig')
apkList = f.readlines()

apkDirs = r'E:\APKDownLoad\normal\22222'    #安卓应用所在文件目录

os.chdir('C:\\Users\sp\\Desktop\\androguard-2.0')
score = open(r"C:\Users\sp\Desktop\cmp\Androguard\score.txt", "a")
result = open(r"C:\Users\sp\Desktop\cmp\Androguard\result.txt", "a")
for line in apkList:
	apkHelp = line.split(':')[0]
	apk = apkHelp.split(',')
	apkName1 = apk[0]
	apkName2 = apk[1]

	try:
		apkPath1 = apkDirs + "\\" + apkName1 + ".apk"+ " "
		apkPath2 = apkDirs + "\\" + apkName2 + ".apk"
		command = r"python androsim.py -i "+ apkPath1 + apkPath2
		f = os.popen(command, "r")
		d = f.read()
		cmdList = d.split("\n")
		try:
			for string in cmdList:
				if string.__contains__("methods:") and string.__contains__("similarities"):
					strList = string.split(" ")
					SimScore = strList[2]
					score.write(apkName1 +" "+ apkName2 + " " + SimScore +'\n')
					SimScore = SimScore.replace('%', '0')
					if float(SimScore) > 60:
						result.write(apkName1 +" "+ apkName2 +": " + SimScore +'\n')
		except:
			CannotCompare = open(r"C:\Users\sp\Desktop\cmp\Androguard\CannotCompare.txt")
			CannotCompare.write(apkName1 +" "+ apkName2)
			CannotCompare.close()
	except:
		print(apkName1 + " " + apkName2)
score.close()
result.close()

