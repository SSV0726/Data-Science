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

df = pd.read_csv("amd.csv")

df2 = pd.read_csv("manual.csv")
df2.head()

open_price =df.iloc[:,1:2]
    
plt.plot(range(1,len(open_price)+1),open_price)
ax = plt.axes()
ax.grid()


plt.savefig('Data_look.png',format='png')
x = df2.iloc[:,1:2].values



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    