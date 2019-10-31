import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
import datetime

data_dir1 = '/Users/yuanjielu/Desktop/CEIE Project/TysonDataset/1-6_col_1.csv'
data_dir2 = '/Users/yuanjielu/Desktop/CEIE Project/TysonDataset/1-6_con_1.csv'
index_name = ['Standardized Type','Start time','Closed time','Location','Duration','Max Lanes Closed']
dataSet1 = pd.read_csv(data_dir1,index_col = 0) # col
dataSet2 = pd.read_csv(data_dir2,index_col = 0) # con

dataSet1['Start time'] = pd.to_datetime(dataSet1['Start time'])
dataSet1['Closed time'] = pd.to_datetime(dataSet1['Closed time'])
dataSet2['Start time'] = pd.to_datetime(dataSet2['Start time'])
dataSet2['Closed time'] = pd.to_datetime(dataSet2['Closed time'])

duringContruction = []
notDuringContruction = []

isConstruction = []
for i in range(len(dataSet1)):
    flag = 0
    for j in range(len(dataSet2)):

        start = (dataSet1['Start time'].iloc[i] - dataSet2['Start time'].iloc[j]).days
        end = (dataSet1['Start time'].iloc[i] - dataSet2['Closed time'].iloc[j]).days
        if int(start) >= 0 and int(end) < 0:
            duringContruction.append(dataSet1.iloc[i].values.tolist())
            flag = 1
            break
    if flag == 0:
        notDuringContruction.append(dataSet1.iloc[i].values.tolist())

duringContruction = pd.DataFrame(duringContruction, columns = index_name)
notDuringContruction = pd.DataFrame(notDuringContruction, columns = index_name)
level_con = pd.value_counts(duringContruction['Duration'])
level_notCon = pd.value_counts(notDuringContruction['Duration'])
print("30,60,120,240")
print(level_con)

print(level_notCon)

# print(duringContruction.info())
# print(notDuringContruction.info())

time = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

print("Collisions for each hour:")
all = pd.value_counts(dataSet1['Start time'].dt.hour,sort = False)
print(all)

print("Collisions for each hour:")
all_1 = pd.value_counts(duringContruction['Start time'].dt.hour,sort = False)
print(all_1)

print("Collisions for each hour:")
all_2 = pd.value_counts(notDuringContruction['Start time'].dt.hour,sort = False)
print(all_2)

print('Collision for week, dataSet1')
weekday = pd.value_counts(dataSet1['Start time'].dt.weekday,sort = False)
print(weekday)

print('Collision for week, duringContruction')
weekday_1 = pd.value_counts(duringContruction['Start time'].dt.weekday,sort = False)
print(weekday_1)

print('Collision for week, duringContruction')
weekday_2 = pd.value_counts(notDuringContruction['Start time'].dt.weekday,sort = False)
print(weekday_2)



plt.plot(time,
         all,
         linestyle = '-',
         linewidth = 2,
         color ='steelblue',
         marker = 'o',
         markersize = 3,
         markeredgecolor = 'black',
         label = 'All'
         )

plt.plot(time,
         all_1,
         linestyle = '-',
         linewidth = 2,
         color ='red',
         marker = 'o',
         markersize = 3,
         markeredgecolor = 'black',
         label = 'Constuction'
         )

plt.plot(time,
         all_2,
         linestyle = '-',
         linewidth = 2,
         color ='green',
         marker = 'o',
         markersize = 3,
         markeredgecolor = 'black',
         label = 'Noconstruction'
         )
plt.ylabel = 'Count each day'
plt.xlabel = 'date'
plt.legend()
plt.show()



plt.plot(week,
         weekday,
         linestyle = '-',
         linewidth = 2,
         color ='steelblue',
         marker = 'o',
         markersize = 3,
         markeredgecolor = 'black',
         label = 'All'
         )

plt.plot(week,
         weekday_1,
         linestyle = '-',
         linewidth = 2,
         color ='red',
         marker = 'o',
         markersize = 3,
         markeredgecolor = 'black',
         label = 'Construction'
         )

plt.plot(week,
         weekday_2,
         linestyle = '-',
         linewidth = 2,
         color ='green',
         marker = 'o',
         markersize = 3,
         markeredgecolor = 'black',
         label = 'Noconstruction'
         )

plt.ylabel = 'Count each day'
plt.xlabel = 'date'
plt.legend()
plt.show()