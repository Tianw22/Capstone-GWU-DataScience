#generate .json for boxradial.js

import numpy as np
import pandas as pd
import datetime as dt

###Import data and only save the columns needed.
file_name =  "film17prevue.xlsx"
df = pd.read_excel(io=file_name)

#Remove all the duplicates by "title", and remain the last record.
dfnew = df.drop_duplicates(subset='title', keep='last')
dfnew.columns = ['title','launch','boxoffice','category','director','duration','cover','actors','abstract','version','grade']

dfboxgra = dfnew[['launch','boxoffice']]
dfboxgra.head()

time = dfboxgra['launch'].astype(str)
month = time.str.slice(5,7)

dfboxgra['month']=month

JAN = dfboxgra[dfboxgra['month']=='01']
FEB = dfboxgra[dfboxgra['month']=='02']
MAR = dfboxgra[dfboxgra['month']=='03']
APR = dfboxgra[dfboxgra['month']=='04']
MAY = dfboxgra[dfboxgra['month']=='05']
JUN = dfboxgra[dfboxgra['month']=='06']
JUL = dfboxgra[dfboxgra['month']=='07']
AUG = dfboxgra[dfboxgra['month']=='08']
SEP = dfboxgra[dfboxgra['month']=='09']
OCT = dfboxgra[dfboxgra['month']=='10']
NOV = dfboxgra[dfboxgra['month']=='11']
DEC = dfboxgra[dfboxgra['month']=='12']

stat1 = JAN["boxoffice"].describe()
stat2 = FEB["boxoffice"].describe()
stat3 = MAR["boxoffice"].describe()
stat4 = APR["boxoffice"].describe()
stat5 = MAY["boxoffice"].describe()
stat6 = JUN["boxoffice"].describe()
stat7 = JUL["boxoffice"].describe()
stat8 = AUG["boxoffice"].describe()
stat9 = SEP["boxoffice"].describe()
stat10 = OCT["boxoffice"].describe()
stat11 = NOV["boxoffice"].describe()
stat12 = DEC["boxoffice"].describe()

stat1 = pd.DataFrame(stat1)
stat1 = stat1.T
stat2 = pd.DataFrame(stat2)
stat2 = stat2.T
stat3 = pd.DataFrame(stat3)
stat3 = stat3.T
stat4 = pd.DataFrame(stat4)
stat4 = stat4.T
stat5 = pd.DataFrame(stat5)
stat5 = stat5.T
stat6 = pd.DataFrame(stat6)
stat6 = stat6.T
stat7 = pd.DataFrame(stat7)
stat7 = stat7.T
stat8 = pd.DataFrame(stat8)
stat8 = stat8.T
stat9 = pd.DataFrame(stat9)
stat9 = stat9.T
stat10 = pd.DataFrame(stat10)
stat10 = stat10.T
stat11 = pd.DataFrame(stat11)
stat11 = stat11.T
stat12 = pd.DataFrame(stat12)
stat12 = stat12.T

frames=[stat1,stat2,stat3,stat4,stat5,stat6,stat7,stat8,stat9,stat10,stat11,stat12]
new = pd.concat(frames)

new = new.reset_index()

new['index']=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

new.columns = ['month','count','mean','std','low','q1','median','q3','high']

out = new[['month','low','q1','median','q3','high']]

dataoutput=out.to_json('C:........../capstone/reactjs/boxradial.json',orient='table')
out.to_json(orient='table')
