#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: __init__.py.py
@time: 2018/12/25/025 21:29
@desc: APP用作相似性比较的文件的拷贝，分别拷贝的是存储资源文件哈希值的DHash文件，
存储权限和组件的AndroidMainifest.xml文件和\res\layout目录下的xml布局文件
其实就是太多的APP应用解压之后文件太大了，存不下那么多的应用
这能把我需要的文件取下来
'''


import os
import os.path
import shutil

##文件夹拷贝
def copytree(src, dst, symlinks=False):
    names = os.listdir(src)
    if not os.path.isdir(dst):
        os.makedirs(dst)
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks)
            else:
                if os.path.isdir(dstname):
                    os.rmdir(dstname)
                elif os.path.isfile(dstname):
                    os.remove(dstname)
                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except OSError as err:
            errors.extend(err.args[0])
    try:
        shutil.copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    if errors:
        # raise Error(errors)
        print(errors)


def copyAndMove(inPath, outPath):
    filePathLists = os.listdir(inPath)
    for path in filePathLists:
        DhashValFileName = inPath + '\\' + path + '\\' + 'DhashVal.txt'
        AndroidManifestFileName = inPath + '\\' + path + '\\' + 'AndroidManifest.xml'
        outAppPath = os.path.join(outPath, path)
        if not os.path.exists(outAppPath):
            os.makedirs(outAppPath)
        try:
            shutil.copy(DhashValFileName, outAppPath)
        except:
            print("there is no such file:" + DhashValFileName)
        try:
            shutil.copy(AndroidManifestFileName, outAppPath)
        except:
            print("there is no such file:" + AndroidManifestFileName)
        res_layout = inPath + '\\' + path + '\\' + "res" + "\\" + "layout"
        copytree(res_layout, outAppPath + '\\' + "res" + "\\" + "layout")


if __name__ == '__main__':
    inPath = r'C:\Users\Song\Desktop\APPVal'
    outPath = r'C:\Users\Song\Desktop\APPPath'
    copyAndMove(inPath, outPath)
