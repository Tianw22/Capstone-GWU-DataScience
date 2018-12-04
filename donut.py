#generate .json for donut.js

import numpy as np
import pandas as pd
import datetime as dt

import numpy as np
import pandas as pd
import datetime as dt

###Import data and only save the columns needed.
file_name =  "film17prevue.xlsx"
df = pd.read_excel(io=file_name)

#Remove all the duplicates by "title", and remain the last record.
dfnew = df.drop_duplicates(subset='title', keep='last')
dfnew.columns = ['title','launch','boxoffice','category','director','duration','cover','actors','abstract','version','grade','level']
donut = dfnew[['launch','level']]


time = donut['launch'].astype(str)
month = time.str.slice(5,7)

donut['month']=month

donut.head()

sizecount = donut.groupby(['month','level']).size()
sizedf = pd.DataFrame(sizecount)
sizedf.reset_index()
sizedf

