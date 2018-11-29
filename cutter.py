#This is a video cutter. Cut every 2 seconds. 
#Cut from specific folder and store in the specific folder, too.
#这是个简单的视频剪切程序。
#每两秒剪切一张图。
#从哪读取的视频存到哪儿去。
#不过，bug在于，输出图片会全部出现在根目录。
#电脑要起飞了，哈，哈，哈。
#That's it.

import cv2
import pandas as pd
from __future__ import division
import shutil, os

file_name =  "filmalllink.xlsx"
film = pd.read_excel(io=file_name)
siz = film['count']

def vcutter(item,a):
    vidcap = cv2.VideoCapture('./prevue/%s/%s.mp4'%(items, a))
    success,image = vidcap.read()
    count = 0
    success = True
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    fps = int(fps)
    while success:
        success,image = vidcap.read()
        #print('read a new frame:',success)
        if count%(2*fps) == 0 :
            cv2.imwrite('%dframe%d.jpg'%(a,count),image)#不知道为什么这里定义不了路径。Couldn't add path here. Don't know why.
            shutil.copy('%dframe%d.jpg'%(a,count), './prevue/%i'%items) #Copied to the right path. 把新生成的文件复制到应在位置。
            print('success')
        count+=1
        
i = 0
nums = siz[i]
a = 0
for items in range(0,len(film['title'])):
    for num in range(nums):
        print("new folder %a"%items) #Have a sense that which folder it being cut
        vcutter(items,a)
        a = a+1
    a = a    
    i=i+1
    nums = siz[i]
    
