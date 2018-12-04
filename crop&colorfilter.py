#It's the combination of cropper and black&white filter.
#Have to do it manuly folder by folder. 
#Have to chose the one to crop as the example of the full folder.
#Have to cut the video if the number of pictures in the folder is too small.
#The cutter is here.


'''Here is the cutter
a = 0
path = './prevue/foldername'
#print('%s/%i.mp4'%(path,i))
for i in range(num1,num2): #num1 is the name[1] of video1 and num2 is the name[1] of video2 +1
    vidcap = cv2.VideoCapture('%s/%i.mp4'%(path,i))
    success,image = vidcap.read()
    count = 0
    #a = 0
    success = True
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    fps = int(fps)
    while success:
        success,image = vidcap.read()
        #print('read a new frame:',success)
        if count%(1*fps) == 0 :
            cv2.imwrite('%d.jpg'%a,image)
            shutil.copy('%d.jpg'%a, path)
            #print('success')
            a=a+1
        count+=1
    a = a
'''


from PIL import Image
import shutil, os 
import cv2
import numpy
import os

#Input the specific number(num) of the folder.
path = './prevue/num'
pathnum = num

#Traverse all the .jpg files.
def filenumcal(path):
    filenum = 0
    for root,dirs,files in os.walk(path): 
            for each in files:
                    if each[-4:] == '.jpg':
                        filenum = filenum+1
    return filenum
    
##Cropper

src_folder = path

def isCrust(pix):
    return sum(pix) < 25

def hCheck(img, y, step = 50):
    count = 0
    width = img.size[0]
    for x in range(0, width, step):
        if isCrust(img.getpixel((x, y))):
            count += 1
        if count > width / step / 2:
            return True
    return False

def vCheck(img, x, step = 50):
    count = 0
    height = img.size[1]
    for y in range(0, height, step):
        if isCrust(img.getpixel((x, y))):
            count += 1
        if count > height / step / 2:
            return True
    return False

def boundaryFinder(img,crust_side,core_side,checker):
    if not checker(img,crust_side):
        return crust_side
    if checker(img,core_side):
        return core_side

    mid = (crust_side + core_side) / 2
    while  mid != core_side and mid != crust_side:
        if checker(img,mid):
            crust_side = mid
        else:
            core_side = mid
        mid = (crust_side + core_side) / 2
    return core_side
    pass

img = Image.open(os.path.join(src_folder,'12.jpg')) # Here is the example picture you want to use.
#img = Image.open(os.path.join(src_folder,filename))
if img.mode != "RGB":
    img = img.convert("RGB")
width, height = img.size

left = boundaryFinder(img, 0, width/2, vCheck)
right = boundaryFinder(img, width-1, width/2, vCheck)
top = boundaryFinder(img, 0, height/2, hCheck)
bottom = boundaryFinder(img, height-1, width/2, hCheck)

rect = (left,top,right,bottom)
print (rect)
for(path,dirs,files) in os.walk(path):                      
        for filename in files:
            ext = os.path.splitext(filename)[1]                 
            if(ext == '.jpg'):                                  
#                 print (filename) 
                img2 = Image.open(os.path.join(src_folder,filename))
                region = img2.crop(rect)
                region.save(os.path.join(src_folder,filename),'PNG')
                
                
def colorave(folder,jpgname):
    count = 0
    myimg = cv2.imread('./prevue/%s/%s.jpg'%(folder,jpgname))
    avg_color_per_row = numpy.average(myimg, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    for a in range(len(avg_color)):
        if avg_color[a] <15: #Totally black is (0,0,0). 纯黑是（0，0，0）
            count = count+1
        elif avg_color[a]>175: 
            count = count+1
    if count==3:
        #print('Check the picture: %i.jpg'%jpgname)
        os.remove('./prevue/%s/%s.jpg'%(folder,jpgname)) # Delete the original one.
    return avg_color

# Traverse all the .jpg files and delete the almost white and almost black picture.
#删除纯黑图片和纯白图片。

filenum = filenumcal(path)   

for(path,dirs,files) in os.walk(path):                      
    for filename in files:
        ext = os.path.splitext(filename)[1] 
        name = os.path.splitext(filename)[0]
        if(ext == '.jpg'): 
            colorave(pathnum,name)
