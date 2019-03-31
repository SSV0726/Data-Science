#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:55:13 2019

@author: Sagar vats

    O+ - Outstanding Retailer = 3
    A - Good Retailer         = 2
    B - Poor Retailer         = 1
    F - Retailer with 0 sales = 0

"""

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

df = pd.read_csv('Case.csv')
df.drop(['Category of Retailer'],axis=1)

retailers=df.iloc[:,0].values
sales=df.iloc[:,13].values   #Total Sales
brands=df.iloc[:,14].values  #Number of Brands

sales_sum=0
cnt=0
for i in range(0,len(retailers)):
    if sales[i]>0:
        sales_sum+=sales[i]
        cnt+=1;
avg = sales_sum/cnt


for i in range(0,len(retailers)):
    if( sales[i]>2*avg ):
        df.at[i,"Category of Retailer"]=3
        df.at[i,"Category_of_Retailer"]="O+"
    if(sales[i]>avg and sales[i]<2*avg and brands[i]>=7):
        df.at[i,"Category of Retailer"]=3
        df.at[i,"Category_of_Retailer"]="O+"
    if(sales[i]>avg and sales[i]<2*avg and brands[i]<7):
        df.at[i,"Category of Retailer"]=2
        df.at[i,"Category_of_Retailer"]="A" 
    if(sales[i]>(avg/2) and sales[i]<avg and brands[i]>=7):
        df.at[i,"Category of Retailer"]=2
        df.at[i,"Category_of_Retailer"]="A" 
    if(sales[i]>0 and sales[i]<avg and brands[i]<7):
        df.at[i,"Category of Retailer"]=1
        df.at[i,"Category_of_Retailer"]="B"  
    if(sales[i]==0):
        df.at[i,"Category of Retailer"]=0
        df.at[i,"Category_of_Retailer"]="F"

# Uncomment the Below part to see the data Visually using Graph
'''

plt.xlabel("Reatiler ID's " )
plt.ylabel("Total Sales")

for i in range(0,len(retailers)):
    if( sales[i]>2*avg ):
        plt.scatter(retailers[i],sales[i],color='green')
    if(sales[i]>avg and sales[i]<2*avg and brands[i]>=7):
        plt.scatter(retailers[i],sales[i],color='green')
    if(sales[i]>avg and sales[i]<2*avg and brands[i]<7):
        plt.scatter(retailers[i],sales[i],color='yellow')
    if(sales[i]>(avg/2) and sales[i]<avg and brands[i]>=7):
        plt.scatter(retailers[i],sales[i],color='yellow')
    if(sales[i]>0 and sales[i]<avg and brands[i]<7):
        plt.scatter(retailers[i],sales[i],color='red')
    if(sales[i]==0):
        plt.scatter(retailers[i],sales[i],color='black')

'''

df.to_csv("Result.csv", index=False)






















