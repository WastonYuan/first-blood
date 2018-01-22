#coding=utf-8
# -*- coding:gb2312 -*- ＃必须在第一行或者第二行

"""
read a file content to a list
"""
def readFile(filePath):
    fileList = []
    file = open(filePath)

    while 1:
        line = file.readline()
        if not line:
            break
        fileList.append(line.strip())
    file.close()
    return fileList


def writeFile(filePath, res_str_list):
    targetFile = open(filePath, 'w')
    for line in res_str_list:
        targetFile.write("%s\n" % line)
    targetFile.close()

def appendFileNewLine(filePath, str):

   hs = open(filePath,"a")
   hs.write(str + '\n')
   hs.close()

if __name__ == '__main__':

    list = readFile("/Users/wangxinyuan/Downloads/教育金融旅游行业高商业价值TERM+-+Sheet1.tsv")
    print type(list)
    for i in list:
        print i