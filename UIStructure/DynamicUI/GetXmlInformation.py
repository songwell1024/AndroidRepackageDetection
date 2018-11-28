#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: GetXmlInformation.py
@time: 2018/11/26/026 14:33
@desc: 获取xml文件的信息
'''

import xml.etree.ElementTree as ET

#获取信息
def getXmlData(file_name):
    level = 0  # 节点的深度从1开始
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, level, result_list)
    return result_list

#遍历xml
def walkData(root_node, level, result_list):
    if (root_node.attrib.__contains__('class')):
        if root_node.attrib['visible-to-user'] == 'false':
            return
        temp_list = [level, root_node.attrib['class']]
        if (root_node.attrib.__contains__('clickable')):
            temp_list.append(root_node.attrib['clickable'])
        if (root_node.attrib.__contains__('bounds')):
            temp_list.append(root_node.attrib['bounds'])
        result_list.append(temp_list)

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        if child.tag == 'node':
            walkData(child, level + 1, result_list)
    return

#获取可点击元素的坐标
def getClickableCoordinate(ele_list):
    coord = []
    for e in ele_list:
        if e[2] == 'true':
            coord.append(stringArrayToIntegerArray(e[3]))
    return coord

#字符串转换为整型数组
def stringArrayToIntegerArray(s):
    res = [];
    s = s.replace("[", "")
    s = s.replace("]", " ")
    s = s.replace(",", " ")
    s = s.split(" ")
    res.append(int(s[0]) + int(abs(int(s[2]) - int(s[0])) / 2));
    res.append(int(s[1]) + int(abs(int(s[3]) - int(s[1])) / 2));
    return res

#写入文件
def writeToTxt(str, fileName):
    f = open(fileName, 'w')
    f.write(str)  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

if __name__ == '__main__':
    # device_id = '71MBBLM2276G'   # 魅族的id
    # d = u2.connect(device_id) # alias for u2.connect_usb('123456f')
    # print(d.info)
    # print(d.device_info)
    # xml = d.dump_hierarchy()
    # print(xml)
    # print(d.current_app())
    fileName = r'C:\Users\Administrator\Desktop\AndroidManifestTxt\demo.xml';
    # # writeToTxt('aaa', fileName)

    # d.click(360/2, 1774 + (1920 - 1774)/2)
    result = getXmlData(fileName)
    print(result)