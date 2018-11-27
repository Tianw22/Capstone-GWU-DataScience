#首先，这个code是为了毕业论文，并非用为不法用途。
#这个code里主要是要获取各个电影的link以及评分。
#后续用link获取票房数据，时长，上映时间，类型。
#然后就可以，做一些数据分析了。

import re
import urllib
from bs4 import BeautifulSoup
import requests
import pandas as pd

#This is important. But, even with user-agent, do not request more than 60 times per mins. 
#爬猫眼数据每分钟不要多于60，IP会被block。大概会被block 8个小时左右？
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

#There are n pages and 30 items per page.
#https://maoyan.com/filmsxxxxxxxxxxx&offset=page（page是个从0开始，以30为倍数的数字）
#每页有30条记录，要爬n页。
page = []
for x in range(0, n): 
    page.append(x * 30)
    
#Get the links of all the films.
#首先把电影的各自的page抓出来。
links = []
linkdetailed = []
if __name__ == "__main__":
    server = 'http://maoyan.com'
    #target = 'http://maoyan.com/films?showType=3&yearId=12&sortId=3&offset=0' #This is the first page. 
    for i in page:
        target = 'http://maoyan.com/films?showType=3&yearId=12&sortId=3&offset=%i' % i
        req = requests.get(url = target,headers = headers) 
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_ = 'channel-detail movie-item-title')
        a_bf = BeautifulSoup(str(div))
        a = a_bf.find_all('a')
        for each in a:
            links.append(server + each.get('href'))
            linkdetailed.append(each.string + server + each.get('href'))
            #links.append(server + each.get('href'))  
            #print(each.string, server + each.get('href'))
#len(links)

#Get the grades of all the films
#然后抓电影评分，其实可以和上面的写在一起。
#开始想进到每个电影的page抓电影信息，结果发现评分其实这个页面就有了的。只是数字被分成了整数（x.）和小数(x)。
nums = []
inte = []
frac = []
if __name__ == "__main__":
    server = 'http://maoyan.com'
    #target = 'http://maoyan.com/films?showType=3&yearId=12&sortId=3&offset=0' #This is the first page. There are 11 pages and 30 items per page.
    for i in page:
        target = 'http://maoyan.com/films?showType=3&yearId=12&sortId=3&offset=%i' % i
        req = requests.get(url = target,headers = headers) 
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_ = 'channel-detail channel-detail-orange')
        i_bf = BeautifulSoup(str(div))
        integer = i_bf.find_all('i',class_ ='integer')
        fraction = i_bf.find_all('i',class_ ='fraction')
        
        for each in integer:
            inte.append(each.string)
        for each in fraction:
            frac.append(each.string)
            
#看看到第几条记录有电影评分，没有评分的就不需要留着了。
print(len(inte))
print(len(frac))
#Delete all the films without grade.
links = links[:319]
linkdetailed = linkdetailed[:319]

#因为数字被分了两部分，那这里就合并一下。
#把'x.'和'x'合并成'x.x'。这里有些tricky。
intedf = pd.DataFrame(inte)
fracdf = pd.DataFrame(frac)
intedf.columns = ['inte']
fracdf.columns = ['frac']
intedf['inte'] = intedf['inte'].astype('str')
fracdf['frac'] = fracdf['frac'].astype('str')
grade = intedf['inte'].str.cat(fracdf['frac'])
grade = pd.DataFrame(grade)

#把爬出来的电影各自的link，评分，都存进一个excel里。大功告成~
linkex = pd.DataFrame(links)
linkdex = pd.DataFrame(linkdetailed)
writer = pd.ExcelWriter('maoyan.xlsx', engine='xlsxwriter')
linkex.to_excel(writer, sheet_name='Sheet1')
linkdex.to_excel(writer, sheet_name='Sheet2')
grade.to_excel(writer, sheet_name='Sheet3')
writer.save()
