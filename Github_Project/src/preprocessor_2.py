import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import datetime

data_dir1 = '/Users/yuanjielu/Desktop/CEIE Project/wholeproject/1-6_col.csv'
data_dir2 = '/Users/yuanjielu/Desktop/CEIE Project/wholeproject/1-6_con.csv'
index_name = ['Standardized Type','Start time','Closed time','Location','Duration','Max Lanes Closed']
dataSet1 = pd.read_csv(data_dir1,index_col = 0) # col
dataSet2 = pd.read_csv(data_dir2,index_col = 0) # con

dataSet1['Start time'] = pd.to_datetime(dataSet1['Start time'])
dataSet1['Closed time'] = pd.to_datetime(dataSet1['Closed time'])
dataSet2['Start time'] = pd.to_datetime(dataSet2['Start time'])
dataSet2['Closed time'] = pd.to_datetime(dataSet2['Closed time'])

isConstruction = []
for i in range(len(dataSet1)):
    for j in range(len(dataSet2)):
        start = (dataSet1['Start time'].iloc[i] - dataSet2['Start time'].iloc[j]).days
        end = (dataSet1['Start time'].iloc[i] - dataSet2['Closed time'].iloc[j]).days
        if int(start) >= 0 and int(end) < 0:
            isCon = 1
            break
        else:
            isCon = 0
    isConstruction.append(isCon)
s=0
h=0
for i in range(len(isConstruction)):
    if isConstruction[i] == 0:
        s += 1
    else:
        h += 1

print(s)
print(h)