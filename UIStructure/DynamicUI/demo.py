#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: demo.py
@time: 2018/12/5/005 9:40
@desc:
'''

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
需要考虑到的问题
1.怎么快速的确定当前页面已经遍历过  通过哈希的方式
2.返回上一级怎么办
3. 跳转到其他应用怎么办

'''
import uiautomator2 as u2
import DynamicUI.GetXmlInformation as GXI
import os
import hashlib

#全局变量xml的存储路径
filePath  = r'C:\Users\Administrator\Desktop\AppXml'

#全局变量
coordCurPosInArray = {0:0, 1:0, 2:0, 3:0, 4:0}  # 当前页面的坐标遍历到了那个位置
xmlHashDict = {}  # 存放xml的hash:level的值

def processAppToGetUIXml(device_id):
    index = 0
    d = u2.connect(device_id)
    # d.click(0, 0)  # 点击屏幕上的某一个固定位置，然后打开该应用  或者是通过adb获取当前安装好的应用，然后通过获取包名来执行应用
    appPackage = d.current_app()['package']  # 打印当前界面对应的app的包名和启动的activity（最好是开始就进入mainActivity）
    fileDir = filePath + '\\' + appPackage;
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    fileName =fileDir+ '\\' + d.current_app()['activity'] + '_' +str(index) + '.xml'
    index = index + 1
    xml = d.dump_hierarchy()  # 获取当前界面的xml信息
    xmlHashDict[getStrHash(xml)] = 0   #把xml文件的hash值添加到数组中，初始层为0层
    writeToTxt(xml,fileName)
    if not (xml.__contains__('text="登录"') or xml.__contains__('text="注册"')):
        clickCoord0 = getClickCoord(fileName)
    for i in range(coordCurPosInArray[0],clickCoord0.__len__()):     #初始层
        coordCurPosInArray[0] = i + 1;
        if d.current_app()['package'] == appPackage:
            d.click(clickCoord0[i][0], clickCoord0[i][1])
            xml = d.dump_hierarchy()
            xmlHash = getStrHash(xml)
            if xmlHashDict.__contains__(xmlHash):
                while(xmlHashDict[xmlHash] > 0):
                    d.press('back')
            else:
                if d.current_app()['package'] == appPackage:
                    fileName = fileDir + '\\' + d.current_app()['activity'] + '_' + str(index) + '.xml'
                    index = index + 1;
                    writeToTxt(xml,fileName)
                    d.press('back')
                else:
                    d.press('back')
        else:
            if d.current_app()['package']=='com.huawei.android.launcher':
                d.app_start(appPackage)     #在初始层界面就点击退出了当前应用时，要返回当前应用，并且退出之后的那个点的坐标下一个开始遍历
                processAppToGetUIXml(device_id)
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

#获取点击的坐标
def getClickCoord(fileName):
    clickCoord = GXI.getClickableCoordinate(GXI.getXmlData(fileName));
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