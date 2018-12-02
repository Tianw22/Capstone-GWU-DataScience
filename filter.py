#The pictures has white or black ones. 
#This code is to build a filter to estimate whether the picture is almost all black or all white.
#I didn't delete the "black" or "white" ones. Because some films has a darker color tone or lighter color tone. 
#图片筛选，筛选（近乎）全黑或者（近乎）全白的图片。
#仅仅筛选出符合全黑或者全白条件的图，而不删除。
#因为有的电影就是颜色比较暗的，最好进行一下人工排查。

import cv2
import numpy
def colorave(folder,jpgname):
    count = 0
    myimg = cv2.imread('./prevue/%a/%a.jpg'%(folder,jpgname))
    avg_color_per_row = numpy.average(myimg, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    for a in range(len(avg_color)):
        if avg_color[a] <15:
            count = count+1
        elif avg_color[a]>175:
            count = count+1
    if count==3:
        print('Check the picture: %i.jpg'%jpgname)
    return avg_color
    
for i in range(0,24):
    colorave(1,i)
#以第一个文件夹为例。
#Take folder 1 as example
           
