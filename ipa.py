#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import os.path

fromFilePath = "/Users/keke/Downloads/wechat"

class FileModel :
    fileType = ""
    fileInfo = 0.00
    fileCounts = 0.0

print "分析ipa 构成"
print "_____________________________________________\n"
index = 1;
sumfileByte = 0.00
filesTypeAry = [FileModel]

for root, dirs, files in os.walk(fromFilePath):
    for name in files:
            fileName, fileSuffix = os.path.splitext(name)
            toFullPath = fromFilePath + root[len(fromFilePath):]
            toFullName = toFullPath + '/' + name
            fileByte = os.path.getsize(toFullName)

            hasModel = False
            tmpmodel = FileModel()

            for model in filesTypeAry :
                if model.fileType == fileSuffix:
                        hasModel = True
                        tmpmodel = model
                else:
                    pass

            if hasModel :
                tmpmodel.fileCounts = tmpmodel.fileCounts + 1
                tmpmodel.fileInfo = fileByte + tmpmodel.fileInfo
            else:
                fmodle = FileModel()
                fmodle.fileCounts = 0.00
                fmodle.fileInfo = 0
                fmodle.fileType = fileSuffix
                fmodle.fileCounts = fmodle.fileCounts + 1
                fmodle.fileInfo = fileByte + fmodle.fileInfo
                filesTypeAry.append(fmodle)

            sumfileByte = sumfileByte + fileByte


print('all file type is :' + str(len(filesTypeAry)) + '  total size is : ' + str(sumfileByte/1024.00) + 'kb   ' + str(sumfileByte/1024/1024) + 'mb')
for model in filesTypeAry :
    print("----------------------------------------------------------------")
    print("file type is :" + model.fileType)
    print("file count is :" + str(model.fileCounts))
    print("file size is : " + str(model.fileInfo/1024) + 'kb'+ "      " + str(model.fileInfo/1024/1024) + 'mb')
    print("That is " + str(round((model.fileInfo/sumfileByte * 100), 4)) + "%")
