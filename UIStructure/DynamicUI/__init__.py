#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/11/22/022 10:07
@desc:
'''
import uiautomator2 as u2
import xml.etree.ElementTree as ET

def writeToTxt(str, fileName):
    f = open(fileName, 'w')
    f.write(str)  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

def getXmlData(file_name):
    level = 1  # 节点的深度从1开始
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, level, result_list)
    return result_list

def walkData(root_node, level, result_list):

    temp_list = [level, root_node.tag]
    result_list.append(temp_list)
    print(root_node.attrib)
    if (root_node.attrib.__contains__('bounds')):
        print(root_node.attrib['bounds'])
    if (root_node.attrib.__contains__('bounds')):
        print((root_node.attrib)['clickable'])

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, level + 1, result_list)
    return

if __name__ == '__main__':
    # device_id = '71MBBLM2276G'   # 魅族的id
    # d = u2.connect(device_id) # alias for u2.connect_usb('123456f')
    # print(d.info)
    # print(d.device_info)
    # xml = d.dump_hierarchy()
    # print(xml)
    # print(d.current_app())
    fileName = r'C:\Users\Administrator\Desktop\AndroidManifestTxt\demo.xml';
    # writeToTxt('aaa', fileName)
    getXmlData(fileName)

    # d.click(360/2, 1774 + (1920 - 1774)/2)
    # result = getXmlData(fileName)
    # print(result)

