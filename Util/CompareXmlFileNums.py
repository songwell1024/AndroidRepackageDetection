import os
import time


def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str)  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close




# def compareXmlFileNums(outFileName):
def compareXmlFileNums():
    fileName = r'E:\APKDataSet\WanDouJiaResults\MyMethods\Final\7\sim.txt'  # 读取相似APK的文件
    fileRead = open(fileName, encoding='UTF-8-sig')
    apkList1 = fileRead.readlines()

    fileName = r'E:\APKDataSet\WanDouJiaResults\FSquaDRA\7\result.txt'  # 读取相似APK的文件
    fileRead = open(fileName, encoding='UTF-8-sig')
    apkList2 = fileRead.readlines()


    for line in apkList1:
        apkHelp = line.split(':')[0]
        if not apkList2.__contains__(apkHelp):
            print(apkHelp)

        # try:
        #     apkPath1 = apkDirs + "\\" + apkName1 + '\\' + "res" + '\\' + "layout"
        #     apkPath2 = apkDirs + "\\" + apkName2 + '\\' + "res" + '\\' + "layout"
        #     xml_list1 = os.listdir(apkPath1)
        #     xml_list2 = os.listdir(apkPath2)
        #     if xml_list1.__len__() == 0 or xml_list2.__len__() == 0:
        #         print(line)
        #         print("length is 0")
        #         continue
        #     if (xml_list1.__len__() <= 200 or xml_list2.__len__() <= 200) \
        #             and ((xml_list1.__len__() * 3) < (xml_list2.__len__()) \
        #                  or xml_list1.__len__() > (xml_list2.__len__() * 3)):
        #         print(line)
        #         continue
        #     if (xml_list1.__len__() > 200 and xml_list2.__len__() > 200) \
        #             and ((xml_list1.__len__() + 100) < (xml_list2.__len__()) \
        #                  or xml_list1.__len__() > (xml_list2.__len__() + 100)):
        #         print(line)
        #         continue
        #
        #     writeToTxt(line, outFileName)
        # except:
        #     print(line)


if __name__ == "__main__":
#     fileName = r'E:\APKDataSet\WanDouJiaResults\MyMethods\Final\4\SimFinal.txt'
    compareXmlFileNums()