#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: DynamicGetUIXml.py
@time: 2018/11/28/028 9:13
@desc: 动态的遍历获取应用的xml文件
'''
import uiautomator2 as u2
import DynamicUI.GetXmlInformation as GXI
import os
import hashlib

#全局变量xml的存储路径
filePath  = r'C:\Users\Administrator\Desktop\AppXml'

def processAppToGetUIXml(device_id):
    xmlHashDict = {}         #存放xml的hash:level的值
    index = 0
    d = u2.connect(device_id)
    appPackage = d.current_app()['package']  # 打印当前界面对应的app的包名和启动的activity（最好是开始就进入mainActivity）
    fileDir = filePath + '\\' + appPackage;
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    fileName =fileDir+ '\\' + d.current_app()['activity'] + '_' +str(index) + '.xml'
    index = index + 1
    xml = d.dump_hierarchy()  # 获取当前界面的xml信息
    xmlHashDict[getStrHash(xml)] = 0   #把xml文件的hash值添加到数组中，初始层为0层
    writeToTxt(xml,fileName)
    clickCoord0 = getClickCoord(fileName)
    for i in range(clickCoord0.__len__()):
        d.click(clickCoord0[i][0],clickCoord0[i][1])
        xml = d.dump_hierarchy()
        xmlHash = getStrHash(xml)
        if xmlHashDict.__contains__(xmlHash):
            if xmlHashDict[xmlHash] > 0:
                d.press('back')
        else:
            if d.current_app()['package'] == appPackage:
                fileName = fileDir + '\\' + d.current_app()['activity'] + '_' + str(index) + '.xml'
                writeToTxt(xml,fileName)
                xmlHashDict[getStrHash(xml)] = 1
                clickCoord1 = getClickCoord(fileName)
                for j in range(clickCoord1.__len__()):
                    d.click(clickCoord0[i][0], clickCoord0[i][1])
                    xml = d.dump_hierarchy()
                    xmlHash = getStrHash(xml)
                    if xmlHashDict.__contains__(xmlHash):
                        if xmlHashDict[xmlHash] > 0:
                            d.press('back')
                    else:
                        if d.current_app()['package'] == appPackage:
                            fileName = fileDir + '\\' + d.current_app()['activity'] + '_' + str(index) + '.xml'
                            writeToTxt(xml, fileName)
                            xmlHashDict[getStrHash(xml)] = 1
                            clickCoord2 = getClickCoord(fileName)
                        else:
                            d.press('back')
            else:
                d.press('back')


#获取设备的信息
def getDeviceInformation(device_id):
    d = u2.connect(device_id)
    print(d.info)  # 应用信息
    print(d.device_info)  # 设备信息
    appInfo = d.current_app()  # 打印当前界面对应的app的包名和启动的activity（最好是开始就进入mainActivity)
    print(appInfo)

#写入文件
def writeToTxt(xml, fileName):
    startStr = '<node index="0" text="" resource-id="" class="android.widget.FrameLayout" package="com.android.systemui"'
    endStr = '<node index="2" text="" resource-id="com.android.systemui:id/panel_holder" ' \
             'class="android.widget.FrameLayout" package="com.android.systemui" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" ' \
             'scrollable="false" long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[0,0][1080,66]" />\r\n  </node>\r\n'

    xml = xml.replace(xml[xml.find(startStr):(xml.find(endStr) + len(endStr))], '')  # 把手机最上方的电量显示栏去掉
    xml = xml.replace('\r\n', '\r')
    # state = 'rotation="0" state=' + '"' + str(2) + '"'  # state表示所在层次的
    # xml = xml.replace('rotation="0"', state)
    f = open(fileName, 'w',encoding='utf-8')
    f.write(xml)  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

#获取点击的坐标
def getClickCoord(fileName):
    clickCoord = GXI.getClickableCoordinate(GXI.getXmlData(fileName));
    # d.click(clickCoord[0][0],clickCoord[0][1])
    return clickCoord

#获取xml的信息
def getXmlInfo(fileName):
    result = GXI.getXmlData(fileName)
    return result

#计算字符串的hash值
def getStrHash(str):
    md5 = hashlib.md5()
    md5.update(bytes(str, encoding='utf-8'))
    return md5.hexdigest()