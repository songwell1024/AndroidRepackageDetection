#!/usr/bin/env python
# encoding: utf-8
'''
@author: WilsonSong
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: songzhiqwer@gmail.com
@software: garner
@file: AppStaticSimlarity.py
@time: 2019/1/2/002 10:37
@desc:  APP的静态相似性
'''
import StaticMethod.ImageHashSimilarity as IHS
import StaticMethod.AccessorialVectorSimilarity as AVS
import StaticMethod.CompentsAndPermissionSimilarity as CAPS
import os


#从文件中读取并进行相似性的比较
def readTxtToArrayAndCompareSimilarity(filePath):
    OutPutSimFile = r'C:\Users\Administrator\Desktop\AppXml\AppSimValue.txt'          # APP的相似性文件
    if os.path.exists(OutPutSimFile):
        os.remove(OutPutSimFile)
    file_path_lists = os.listdir(filePath)
    for path in file_path_lists:
        paths = filePath + '\\' + path
        apk_lists = os.listdir(paths)
        if apk_lists.__len__() >= 2:
            #辅助特征向量相似性
            vector_fileName1 = paths + '\\' + apk_lists[0] + '\\' + 'AccessorialVector.txt'
            vector_fileName2 = paths + '\\' + apk_lists[1] + '\\' + 'AccessorialVector.txt'
            vectorSimVal = AVS.readTxtToArrayAndCompareSimilarity(vector_fileName1,vector_fileName2)

            #图片资源相似性
            imgHash_fileName1 = paths + '\\' + apk_lists[0] + '\\' + 'DhashVal.txt'
            imgHash_fileName2 = paths + '\\' + apk_lists[1] + '\\' + 'DhashVal.txt'
            imgHashSimVal = IHS.compareImgSimilarity(imgHash_fileName1, imgHash_fileName2)

            #组件和权限相似性
            CP_fileName1 = paths + '\\' + apk_lists[0] + '\\' + 'AndroidManifest.xml'
            CP_fileName2 = paths + '\\' + apk_lists[1] + '\\' + 'AndroidManifest.xml'
            CPSimVal = CAPS.compareSimilarityByComponentsAndPermission(CP_fileName1, CP_fileName2);

            simVal = apk_lists[0] + ', ' + apk_lists[1]+ ':  ' + vectorSimVal +'  ' + imgHashSimVal + ' ' + str(CPSimVal)
            writeToTxt(simVal,OutPutSimFile)
        else:
            print(path)      #找到那些有问题的路径


def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close