#generate .json for wordcloud.js

import numpy as np
import pandas as pd
import datetime as dt

###Import data and only save the columns needed.
file_name =  "wordcloud.xlsx"
df = pd.read_excel(io=file_name)

df = df.dropna()

df = df.reset_index()

sizecount = df.groupby(['genre']).size()
sizedf = pd.DataFrame(sizecount)
sizedf.reset_index()
sizedf.columns = ['size']
#sizedf

dataoutput=sizedf.to_json('C:......./capstone/reactjs/wordcloud.json',orient='table')
sizedf.to_json(orient='table')
