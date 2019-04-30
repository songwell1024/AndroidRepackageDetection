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
import DynamicMethod.DynamicUI.DynamicGetUIXml as DGX
import DynamicMethod.DynamicUI.demo as DD
import DynamicMethod.DynamicUI.test as test
# from lshash import lshash
# import falconn

if __name__ == '__main__':
    # device_id = 'WTKDU16629012163'  # 荣耀的id
    # test.test(device_id)
    ele1 =  {1,2,3,4,5}
    print(ele1.__len__())

    # DD.processAppToGetUIXml(device_id)
    # d = u2.connect(device_id)
    # print(d.info)
    # d.click_post_delay  =10     # 每次点击的等待的时间
    # xml = d.dump_hierarchy()  # 获取当前界面的xml信息
    # print(xml.__contains__("关闭"))
    # print(d.current_app())
    # print(xml.__contains__('取消'))
    #
    # d(text="取消").click();               #点击取消

    # d.app_start(appPackage)  # 在初始层界面就点击退出了当前应用时，要返回当前应用，并且退出之后的那个点的坐标下一个开始遍历
    # d.healthcheck()    #检查并维持设备端守护进程处于运行状态
    # test.test(device_id)  #测试当前界面的输出的






