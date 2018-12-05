#resize and reshape all the merged pics into 600*400
#把文件夹中所有图片缩放到统一尺寸。

from PIL import Image 
import os

for i in range(0,n):#n is the number of pics.
    im = Image.open('./merge/%i.png'%i) #So my dir is ./merge
    out = im.resize((600,400))
    out.save(os.path.join('./merge',os.path.basename('./merge/%i.png')%i)) #overwrite the original pics.
    print('%i is ready'%i)
