#https://blog.csdn.net/u012319493/article/details/75911554 
#搬运别人的码，瞬间批量产出所定数量的空文件夹
import os, sys

base = './name'
#'name' is the name of folders. Define the path here. 
#'name'是文件夹的名字，后缀就是从i=1开始的数字。这里也可以定义文件夹位置。
i = 1
for j in range(n): 
#n is the number of folders.
#n就是所需空文件夹的个数。
    file_name = base + str(i)
    os.mkdir(file_name)
    i=i+1
    
#运行时一定要慎重，把n设置小一点，万一哪儿出错了还能改。
