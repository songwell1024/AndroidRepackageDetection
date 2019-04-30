#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: test.py
@time: 2018/12/5/005 14:20
@desc:
'''

import uiautomator2 as u2
import DynamicMethod.DynamicUI.GetXmlInformation as GXI
import os
import hashlib
import time


filePath  = r'C:\Users\Song\Desktop\AppXml'
def test(device_id):
    index = 0
    d = u2.connect(device_id)
    appPackage = d.current_app()['package']  # 打印当前界面对应的app的包名和启动的activity（最好是开始就进入mainActivity）
    fileDir = filePath + '\\' + appPackage;
    helpXmlName = fileDir + '\\' + 'help.xml'  # 辅助文件，用来每次存取当前遍历界面的布局树
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    fileName = fileDir + '\\' + d.current_app()['activity'] + '_' + str(index) + '_' + '0' + '.xml'
    index = index + 1
    xml = d.dump_hierarchy()  # 获取当前界面的xml信息
    writeToTxt(xml, fileName)
    node_list = GXI.getXmlData(fileName)
    clickCoord0 = getClickCoord(node_list)
    print(clickCoord0)



#写入文件
def writeToTxt(xml, fileName):
    startStr = '<node index="0" text="" resource-id="" class="android.widget.FrameLayout" package="com.android.systemui"'
    endStr = '<node index="3" text="" resource-id="com.android.systemui:id/scrim_in_front" class="android.view.View" package="com.android.systemui" content-desc="" ' \
             'checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" ' \
             'long-clickable="false" password="false" selected="false" visible-to-user="true" bounds="[0,0][1080,72]" />\r\n  </node>\r\n'

    xml = xml.replace(xml[xml.find(startStr):(xml.find(endStr) + len(endStr))], '')  # 把手机最上方的电量显示栏去掉
    xml = xml.replace('\r\n', '\r')
    # state = 'rotation="0" state=' + '"' + str(2) + '"'  # state表示所在层次的
    # xml = xml.replace('rotation="0"', state)
    f = open(fileName, 'w',encoding='utf-8')
    f.write(xml)  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

def getClickCoord(node_list):
    clickCoord = GXI.getClickableCoordinate(node_list);
    return clickCoord

