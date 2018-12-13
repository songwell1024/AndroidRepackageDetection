#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/11/22/022 10:07
@desc: 主函数
'''
import uiautomator2 as u2
import DynamicUI.DynamicGetUIXml as DGX
import DynamicUI.demo as DD

if __name__ == '__main__':
    device_id = 'WTKDU16629012163'  # 荣耀的id
    DD.processAppToGetUIXml(device_id)
    # d = u2.connect(device_id)
    # xml = d.dump_hierarchy()  # 获取当前界面的xml信息
    # print(d.current_app()['package'])
    # print(xml.__contains__('取消'))
    #
    # d(text="取消").click();               #点击取消



