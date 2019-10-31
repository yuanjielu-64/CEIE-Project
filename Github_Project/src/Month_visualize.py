import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_dir1 = '/Users/yuanjielu/Desktop/CEIE Project/wholeproject/col2.csv'
data_dir2 = '/Users/yuanjielu/Desktop/CEIE Project/wholeproject/con2.csv'
index_name = ['Standardized Type','Start time','Closed time','Location','Duration','Max Lanes Closed']

I495 = []
I495_con = []
I66 = []
I66_con =[]
VA7 = []
VA7_con = []

dataSet1 = pd.read_csv(data_dir1,index_col = 0)
dataSet2 = pd.read_csv(data_dir2,index_col = 0)
Sta = dataSet1['Location']
Con = dataSet2['Location']

for i in range(len(Sta)):
    if 'I-495' in Sta[i]:
        I495.append(dataSet1.iloc[i].values.tolist())
    elif 'I-66' in Sta[i] and 'I-664' not in Sta[i]:
        I66.append(dataSet1.iloc[i].values.tolist())
    elif 'VA-7' in Sta[i]:
        VA7.append(dataSet1.iloc[i].values.tolist())

for i in range(len(Con)):
    if 'I-495' in Con[i]:
        I495_con.append(dataSet2.iloc[i].values.tolist())
    elif 'I-66' in Con[i] and 'I-664' not in Con[i]:
        I66_con.append(dataSet2.iloc[i].values.tolist())
    elif 'VA-7' in Con[i]:
        VA7_con.append(dataSet2.iloc[i].values.tolist())


I495 = pd.DataFrame(I495,columns = index_name)
I495_con = pd.DataFrame(I495_con,columns = index_name)
I495['Start time'] = pd.to_datetime(I495['Start time'])
I495_con['Start time'] = pd.to_datetime(I495_con['Start time'])

I66 = pd.DataFrame(I66,columns = index_name)
I66_con = pd.DataFrame(I66_con,columns = index_name)
I66['Start time'] = pd.to_datetime(I66['Start time'])
I66_con['Start time'] = pd.to_datetime(I66_con['Start time'])

VA7 = pd.DataFrame(VA7,columns = index_name)
VA7_con = pd.DataFrame(VA7_con,columns = index_name)
VA7['Start time'] = pd.to_datetime(VA7['Start time'])
VA7_con['Start time'] = pd.to_datetime(VA7_con['Start time'])


count = pd.value_counts(I66['Start time'].dt.day,sort = False)
count = pd.DataFrame({'date':np.unique(I66['Start time'].dt.day),'Count':count})
print(count)

count_con = pd.value_counts(I66_con['Start time'].dt.day,sort = False)
count_con = pd.DataFrame({'date':np.unique(I66_con['Start time'].dt.day),'Count':count_con})


plt.plot(count.date,
         count.Count,
         linestyle = '-',
         linewidth = 2,
         color ='steelblue',
         marker = 'o',
         markersize = 6,
         markeredgecolor = 'black',
         label = 'col'
         )

plt.plot(count_con.date,
         count_con.Count,
         linestyle = '--',
         linewidth = 2,
         color ='indianred',
         label = 'con'
         )

plt.ylabel = 'Count each day'
plt.xlabel = 'date'
plt.legend()
plt.show()