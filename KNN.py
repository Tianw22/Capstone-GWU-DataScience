#Try a simple KNN with the merged data.

import os
import numpy as np
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import shutil, os
import statistics
import random
from sklearn import neighbors
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
import cv2

file_name =  "filmalllink.xlsx"
film = pd.read_excel(io=file_name)
filmnew = film['grade']
filmnew = pd.DataFrame(filmnew)

plt.hist(filmnew['grade'], bins='auto')
plt.title("Histogram of grades")
plt.show()

gradelist = filmnew['grade']
gradelist = pd.to_numeric(gradelist)
for i in range(0,len(gradelist)):
    filmnew['level']=0
    filmnew['index'][i]=i

for i in range(0,len(gradelist)):
    if gradelist[i]<6.0:
        filmnew['level'][i]=0
    elif gradelist[i]<7.0 and gradelist[i]>=6.0:
        filmnew['level'][i]=1
    elif gradelist[i]<8.0 and gradelist[i]>=7.0:
        filmnew['level'][i]=2
    elif gradelist[i]<9.0 and gradelist[i]>=8.0:
        filmnew['level'][i]=3
    else:
        filmnew['level'][i]=4
        
print(filmnew.head())
writer = pd.ExcelWriter('level.xlsx')
filmnew.to_excel(writer,'Sheet1')
writer.save()

plt.hist(filmnew['level'], bins='auto')
plt.title("Histogram of levels")
plt.show()

def levellen(level):
    count = 0
    for ele in filmnew['level']:
        if ele == level:
            count = count+1
    return count
    
l1 = levellen(0)
l2 = levellen(1)
l3 = levellen(2)
l4 = levellen(3)
l5 = levellen(4)
print(l1,l2,l3,l4,l5)

testsize1 = round(l1*0.2)
testsize2 = round(l2*0.2)
testsize3 = round(l3*0.2)
testsize4 = round(l4*0.2)
testsize5 = round(l5*0.2)
print(testsize1,testsize2,testsize3,testsize4,testsize5)

data   = []
labels = filmnew['level']

for i in range(0,203):
    img = Image.open('./merge/%i.png'%i)
    dt = np.array(img.getdata())
    data.append(dt)
    
labels = np.array(labels)
x = np.array(data)
nsamples, nx, ny = x.shape
x = x.reshape((nsamples,nx*ny))
y = labels
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

clf = neighbors.KNeighborsClassifier(algorithm='kd_tree')
clf.fit(x_train, y_train)

answer = clf.predict(x)
print(x)
print(answer)
print(y)
print(np.mean( answer == y))
