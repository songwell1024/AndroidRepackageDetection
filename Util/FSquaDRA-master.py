# -*- coding: utf-8 -*-
import os

jarPath = r"C:\Users\sp\Downloads\FSquaDRA-master\out\artifacts\FSquaDRA_master_jar\FSquaDRA-master.jar "
apkDirs = r"E:\APKDownLoad\WanDouJiaNormal"
myList = os.listdir(apkDirs)
# ignoring = open(r"C:\Users\sp\Desktop\cmp\ignoring.txt", "a")
# result = open(r"C:\Users\sp\Desktop\cmp\result.txt", "a")

for apkName1 in myList[:-1]:
	ignoring = open(r"C:\Users\sp\Desktop\cmp\FSquaDRA\ignoring.txt", "a")
	result = open(r"C:\Users\sp\Desktop\cmp\FSquaDRA\result.txt", "a")
	for apkName2 in myList[myList.index(apkName1)+1:]:
		try:
			apkPath1 = apkDirs + "\\" + apkName1 + " "
			apkPath2 = apkDirs + "\\" + apkName2 + " "
			resultPath = r"-o=C:\Users\sp\Desktop\cmp\FSquaDRA\tmp.txt"
			command = r"java -jar " + jarPath + apkPath1 + apkPath2 + resultPath
			f = os.popen(command, "r")
			d = f.read()
			cmdList = d.split("\n")
			if cmdList[cmdList.index("Skipped files:") + 1] == apkName1:
				ignoring.write(apkName1 + "\n")
				# print(d)
				break
			cmdList.reverse()
			if cmdList[cmdList.index("Skipped files:") - 1] == apkName2:
				# myList.remove(apkName2)
				ignoring.write(apkName2 + "\n")
				# print(d)
				continue
			tmp = open(r"C:\Users\sp\Desktop\cmp\FSquaDRA\tmp.txt", encoding='UTF-8-sig')
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
