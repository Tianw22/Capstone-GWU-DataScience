import urllib.request
import re
import os
import pandas as pd
import urllib
import time

file_name =  "xxxxx.xlsx"
links = pd.read_excel(io=file_name)

#Add a 'http://' head for each link.
#给列表中每个元素加上同样的字符串。
#爬到的链接没有'http://'，整体加一下。
newlist = links.link
head = 'http://'
for i in range(len(newlist)):
    newlist[i] = head + newlist[i]
links['fulllink'] = newlist
#print(newList)

#Anti-block, hahaha. Split the list into shorter lists.
#把list按50一列的间隔进行分割。
title = links["title"]
link = links["fulllink"]
step = 50
titlenew = [title[i:i+step] for i in range(0,len(title),step)]
linknew = [link[i:i+step] for i in range(0,len(link),step)]

#每下完一个小list，停止60秒，再进行下一个list的批量下载。
#url批量下载.mp4，输出名字从0开始。
a=0
for i in range(0,len(linknew)): 
    for url in linknew[i]:
        urllib.request.urlretrieve(url, "%(name)a.mp4"%{'name':a})
        a=a+1
        print("Saved")
    time.sleep(60) #sleep 60 seconds.停止60秒再继续下一个list。
    print("Start new list")
