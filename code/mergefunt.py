def mergepic(foldername,picexname):
    path = './prevue/%i'%foldername
    img = Image.open('%s/%s.jpg'%(path,picexname))
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
    picmaxnum=np.square(numline)
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
