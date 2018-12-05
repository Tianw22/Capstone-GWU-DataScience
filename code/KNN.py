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



######################################################################################################################################
#Generate a average color array. Each pic only has one 1*3 array.
#Build the funtion to get the average color of a pic
def avecolor(n):
    img = cv2.imread('./merge/%i.png'%n)
    b, g, r = cv2.split(img)

    total = img.size / 3 
    B = float(np.sum(b)) / total 
    G = float(np.sum(g)) / total 
    R = float(np.sum(r)) / total 
    Bm = list()
    Gm = list()
    Rm = list()
    Bm.append(B)
    Gm.append(G)
    Rm.append(R)
    b = [Bm[0],Gm[0],Rm[0]]
    return b

c=[]
for i in range(0,203):
    b = avecolor(i)
    c.append(b)
    
for i in range(0,203):
    plt.imshow([(c[i][0],c[i][1],c[i][2])])
    plt.show()
    
labels = np.array(labels)
x2 = np.array(c)
y2 = labels

x_train2, x_test2, y_train2, y_test2 = train_test_split(x2, y2, test_size = 0.2)
clf = neighbors.KNeighborsClassifier(algorithm='kd_tree')
clf.fit(x_train2, y_train2)

result2 = clf.predict(x2)
print(result2)
print(y2)
print(np.mean( result2 == y2))

###################################################################################################################################
plt.scatter(x_train2[:,0], y_train2)
plt.show()
plt.scatter(x_train2[:,1], y_train2)
plt.show()
plt.scatter(x_train2[:,2], y_train2)
plt.show()
plt.scatter(x_test2[:,0], y_test2)
plt.show()
plt.scatter(x_test2[:,1], y_test2)
plt.show()
plt.scatter(x_test2[:,2], y_test2)
plt.show()
