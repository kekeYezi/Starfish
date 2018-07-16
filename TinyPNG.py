#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import tinify
import os
import os.path

tinify.key = "234-zhwWJVU50Y7X8b3FYEFtx8xWzVQv"
fromFilePath = ""

print "压缩图片脚本开始"
print "_____________________________________________\n"
index = 1;
sumOldfileByte = 0
sumnewfileByte = 0

for root, dirs, files in os.walk(fromFilePath):
	for name in files:
		fileName, fileSuffix = os.path.splitext(name)
		if fileSuffix == '.png' or fileSuffix == '.jpg':
                    toFullPath = fromFilePath + root[len(fromFilePath):]
                    toFullName = toFullPath + '/' + name
                    fileByte = os.path.getsize(toFullName)
                    if fileByte > 1024*20 :
                        print "正在处理第" + str(index) + "图片:"
                        print toFullName
                        print("压缩前体积:")
                        print('%d Bytes'%(os.path.getsize(toFullName)))
                        sumOldfileByte = sumOldfileByte + os.path.getsize(toFullName)
                        index = index + 1
                        try:
                            source = tinify.from_file(toFullName)
                            source.to_file(toFullName)
                        except:
                            pass
                        print("压缩后体积:")
                        print('%d Bytes'%(os.path.getsize(toFullName)))
                        sumnewfileByte = sumnewfileByte + os.path.getsize(toFullName)

print "\n_____________________________________________"
print("压缩前总体积:    " + str(sumOldfileByte) + "byte  " + "约  " + str(sumOldfileByte/1024) + "kb  " + str(sumOldfileByte/1024/1024) + "mb")
print("压缩后总体积:    " + str(sumnewfileByte) + "byte  " + "约  " + str(sumnewfileByte/1024) + "kb  " + str(sumnewfileByte/1024/1024) + "mb")
print("压缩减少体积:    " + str(sumOldfileByte - sumnewfileByte) + "byte" + "约  " + str((sumOldfileByte - sumnewfileByte)/1024) + "kb")
print "\n_____________________________________________"
print "压缩图片脚本结束"
