# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:57:31 2019

@author: admin
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import xlwt 
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

#Reading the dataset
df = pd.read_csv("amd.csv")             
df.head()

#converting to array
X=df.iloc[:,:-1].values

#Extracting relevant data according to our Logic
df['High-Low']=df['High']
df['High-Low']=df['High-Low']-df['Low']
df['OpenNx']=df['Open'].shift(-1)
df['Close-OpenNx']=df['Close']
df['Close-OpenNx']=df['Close-OpenNx']-df['OpenNx']

O_p=df.iloc[:-1,1:2]

cmo =df.iloc[:-1,-1:].values        #cmo = Close-minus-Open
hml =df.iloc[:-1,-3:-2].values      #hmo = High-minus-Low
# converting to a standard
hml=hml*1000
cmo=cmo*1000

dt= df.iloc[:, 0:1]

for i in range(0,len(cmo)):
    if(cmo[i]==0):
        cmo[i]=1
    if(cmo[i]<0):
        cmo[i]=cmo[i]*-1

res = cmo*hml

avg_res=sum(res)/len(res)
plt.plot(range(0,len(res)),res)

avg_cmo=sum(cmo)/len(cmo)
avg_hml=sum(hml)/len(hml)

avg_res2=avg_cmo*avg_hml
print(avg_res ,avg_res2)

std_res=np.std(res)
print(std_res)

plt.xlabel('Dates in Increasing order ')
plt.ylabel('Change / Event prediction')
ax=plt.axes()
ax.grid()
plt.show()
        
v=std_res                                   # Scale to Determine which should be considered as events
v=v*6
ln=[v]*len(res)

plt.plot(range(0,len(res)),ln,'g--')


plt.savefig('Event_Pred.png',format='png')

print(" Some Event has Happend on date:")   # Printing the result Obtained 
cnt=0
for i in range(0,len(res)):
    if(res[i]>(v)):
        res[i]=1
        cnt=cnt+1
        print(X[i,0])
    else:
        res[i]=0


# under Development : to extract data to a file 
sheet1.write(0, 0, 'Event') 
with open("out_data.csv","w") as out_file:
    for i in range(1,len(res)):
        sheet1.write(i,0, str(res[i])) 

wb.save("sample.xls") 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
