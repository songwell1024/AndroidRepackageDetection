def writeToTxt(str,fileName):
    f = open(fileName, 'a')   #打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    f.write(  str +'\n')  # 这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    f.close()  # 特别注意文件操作完毕后要close

if __name__ == "__main__":
    fr = open(r'C:\Users\Song\Desktop\1\99999.txt',encoding='UTF-8-sig')
    data = []
    for line in fr.readlines():
        line = line.strip('\n')
        if not data.__contains__(line):
            try:
                writeToTxt(line,r'C:\Users\Song\Desktop\1\22.txt')
            except:
                print(line)
            data.append(line)