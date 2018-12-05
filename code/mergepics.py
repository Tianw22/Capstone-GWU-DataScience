#Merge all the pics into one large pic.
#马赛克式合并图片。想合并多少图就合并多少图。
#按图片原比例合并。

import os
from PIL import Image
import numpy as np

path = './prevue/0'
img = Image.open('%s/1.jpg'%path)
imgwidth = img.size[0]
imgheight = img.size[1]

all_path = []
num = 0

filenum = 0
for root,dirs,files in os.walk(path): 
        for each in files:
                if each[-4:] == '.jpg':
                    all_path.append(os.path.join(root, each))
                    filenum = filenum+1

numline = int(np.sqrt(filenum))
pic_max=np.square(numline)

toImage = Image.new('RGBA',(imgwidth*numline,imgheight*numline))


for i in range(0,numline): 
    for j in range(0,numline):
        pic_fole_head =  Image.open(all_path[num])
        width,height =  pic_fole_head.size
        tmppic = pic_fole_head.resize((imgwidth,imgheight))
        loc = (int(i%numline*imgwidth),int(j%numline*imgheight))
        toImage.paste(tmppic,loc)
        num= num+1
        if num>pic_max:
            break
print(toImage.size)
toImage.save('%s/merged.png'%path)
