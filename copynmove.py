#I downloaded all the prevues in one folder. It made life harder.
#So, it would be better to put the prevues of one film in one folder.
#Then, this step made my life harder again.
#如何骚气的用python整理文件夹。
#下载预告片时候，把所有的预告片从0开始编号，下载到了同一个文件夹里。
#头大的是，每个电影不止一个预告片，而是，看片方心情，有的电影有一个预告片，而有的，竟然可以有将近20个。呵呵。
#这个code就是要把不同电影的预告片放到所在电影的文件夹里。
#这一波骚气的操作有利于后续的视频切割。
#话不多说。code在此。
#shutil made my life easier. YAY~!

import pandas as pd
import numpy as np
import shutil, os

file_name =  "xxxxxxx.xlsx"
film = pd.read_excel(io=file_name)
#film.head(5)
film = film.reset_index() 
#'d better reset index. Or the index will play trick on you.
#最好把index给重新set一下，不然后续会引起不必要的麻烦。
#film
siz = film['size']
#siz

i = 0
nums = siz[i]
a = 0
for items in range(0,len(film['title'])):
    for num in range(nums):
        print(a)#这里可以知道运行到第几个视频了，a从0开始编号，和视频编号一样的。
        shutil.copy('./pre/%a.mp4'%a, './prevue/%i'%items) 
        #把./pre/里的.mp4 按名字顺序遍历，并按每个电影的预告片数量复制相应数量的预告片到./prevue/里从0开始编号的文件夹里。
        #保证所有数据的顺序一致很重要。
        a = a+1
        #a的定义很重要，这样可以呼应预告片从0开始的名字，不然遍历过程中，每次都会从0开始，就不能match了。
    a = a    
    i=i+1
    nums = siz[i]
    print("new folder")#这里就是个小提示。嗨！下一个文件夹开始了哦！
        
        
