#groupby will sort the data into a new order.
#Then I found Excel could do the same groupby thing and gave the size. But, had to split the new column into two. 
#Because all the names had a "count" suffix.
#Then life is easier again.
#用groupby时候，顺序会变，懒人一只的我为了节省时间，就用excel的subtotal+count function. 
#再用python去掉NA行，剩下的就是，电影名和预告片数量，这两列数据了。

import pandas as pd
import numpy as np

file_name =  "newprevue.xlsx" #newprevue.xlsx就是用excel处理后的表格。
newsheet = pd.read_excel(io=file_name2)
newsheet = newsheet.dropna() #drop all the na lines. 去掉所有带na值的行。

writer = pd.ExcelWriter('prevuensize.xlsx')
newsheet.to_excel(writer,'Sheet1')
writer.save()
#save into a new '.xlsx' for further uses.
