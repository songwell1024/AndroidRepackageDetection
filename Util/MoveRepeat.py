import os

def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

def moveRepeat(filePath):
    fileList = os.listdir(filePath)
    for file in fileList:
        DhashTXT = filePath + "\\" + file + "\\" + "DhashVal.txt"
        try:
            f = open(DhashTXT)
            HashSet = f.readlines()
            f.close()
            os.remove(DhashTXT)
            Data = []
            for val in HashSet:
                val = val.strip("\n")
                if not Data.__contains__(val):
                    Data.append(val)
                    writeToTxt(val,DhashTXT)
        except:
            print(file)






if __name__ == "__main__":

    filePath = r'E:\APKDataSet\wandoujiaAPK\Decompile\1'
    moveRepeat(filePath)
    filePath2 = r'E:\APKDataSet\wandoujiaAPK\Decompile\2'
    moveRepeat(filePath2)