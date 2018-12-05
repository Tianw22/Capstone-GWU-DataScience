#groupby will sort the data into a new order.
#Then I found Excel could do the same groupby thing and gave the size. But, had to split the new column into two. 
#Because all the names had a "count" suffix.
#Then life is easier again.
#用groupby时候，顺序会变，懒人一只的我为了节省时间，就用excel的subtotal+count function. 
#再用python去掉NA行，剩下的就是，电影名和预告片数量，这两列数据了。

import pandas as pd
import numpy as np

file_name2 =  "prealllinks.xlsx"#prealllinks.xlsx就是用excel处理后的表格。
newsheet = pd.ExcelFile(io=file_name2)
newsheet = newsheet.parse('Sheet4')
#newsheet = newsheet[['count','title']]#only select the columns needed. 选择列。
#newsheet

newsheet = newsheet.dropna()#drop all the na lines. 去掉所有带na值的行。
#newsheet.index
newsheet.reset_index(drop=True)
newsheet.set_index('title', inplace=True)#reset index from 0. 从0重新定义index。
#newsheet

file_name3 =  "film17.xlsx"
newsheet2 = pd.ExcelFile(io=file_name3)
newsheet2 = newsheet2.parse('Sheet1')
newsheet2.columns = ['link','detail','grade','title']

newsheet2.reset_index()
newsheet2.set_index('title', inplace=True)
#newsheet2

#用title列进行合并。combine the two dataframe by colomn"title".
result = pd.concat([newsheet, newsheet2],axis=1, join_axes=[newsheet.index])
#result

writer = pd.ExcelWriter('filmalllink.xlsx')
result.to_excel(writer,'Sheet1')
writer.save()
#save into a new sheet of 'filmalllinks.xlsx' for further uses.
#this dataset has film's page link, its grade and the count of its prevues.
