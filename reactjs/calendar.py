#generate .json for react.js

import numpy as np
import pandas as pd
import datetime as dt

###Import data and only save the columns needed.
file_name =  "film17prevue.xlsx"
df = pd.read_excel(io=file_name)

#Remove all the duplicates by "title", and remain the last record.
dfnew = df.drop_duplicates(subset='title', keep='last')
dfnew.columns = ['title','launch','boxoffice','category','director','duration','cover','actors','abstract','version','grade']

dfboxgra = dfnew[['launch','boxoffice','grade']]
dfboxgra = dfboxgra.set_index('launch')
dfboxgra.head()

datedet = dfboxgra.groupby(['launch']).size()

datedet = pd.DataFrame(datedet)
datedet.head()

datedet = datedet.reset_index()
datedet.columns=['launch','release']

time = datedet['launch'].astype(str)

month = time.str.slice(5,7)

datedet['month']=month
datedet['day']=datedet['launch'].dt.dayofweek
datedet['week']=datedet['launch'].dt.week

datedet['week'][0]=1
#datedet

dataoutput=datedet.to_json('path/capstone/reactjs/calendar.json',orient='table')
