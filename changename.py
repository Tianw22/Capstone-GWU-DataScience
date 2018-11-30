import os  

def rename(foldername): 
    path = './prevue/%a'%foldername
    #print(path) #
    FM = '.jpg' 
    #print (FM)  
    i = 0                                              
    for(path,dirs,files) in os.walk(path):# Read the files                     
        for filename in files: #For loop to traverse all the files.                               
            ext = os.path.splitext(filename)[1]#Split the file name.
            name = i #Name all the files from 0 by order. 从0开始命名。
            if(ext == FM):  #Only rename the ones with the same ext. 只重命名拓展名为.jpg的文件。                                 
                #print (filename) 
                #print (name)                                       
                newname = str(int(name)) + FM #New name forms here. x.jpg. x is from 0 by order. 命名新名字从0开始，名字是数字.jpg。
                oldpath = path + "//" + filename #Old path. 源文件路径。
                newpath = path + "//" + newname #New path. 新文件路径。
                try: 
                    os.rename(oldpath,newpath)#Rename here. 重命名部分。
                except BaseException:
                    print(str(e))
                print (newpath)  
                i = i+1 
                
                
for i in range(0,203):
#一共有203个文件夹，把所有文件夹里的图片都进行从0开始的重命名。
#Rename all the .jpg in 203 folders. The pics in each folder name begin with 0.
    rename(i)
