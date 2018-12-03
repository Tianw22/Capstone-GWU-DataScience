#This is the image cropper. 
#Decide the boarder of an example, then cut all the pictures in the same size.
#剪切图片（处理黑边问题）。检查图片的边界位置。
#如果把整个文件夹里的图片做遍历并剪辑的话，会因为图片本身颜色出现识别问题，边界可能不不同。
#截图就会大小不懂。所有，顶一个rect（也就是一个截图示例），并按这个剪切文件夹里所有图片就好了。
#保证里截图大小相同。


tar_folder = "tar"
backup_folder = "backup"
path = './prevue/0/'
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

os.mkdir('./tar/1')
img = Image.open(os.path.join(src_folder,'2.jpg'))
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
                region.save(os.path.join('./tar/0',filename),'PNG')
