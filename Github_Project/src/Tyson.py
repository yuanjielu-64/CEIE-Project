import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_dir1 = '/Users/yuanjielu/Desktop/CEIE Project/wholeproject/col6.csv'
data_dir2 = '/Users/yuanjielu/Desktop/CEIE Project/wholeproject/con6.csv'
index_name = ['Standardized Type','Start time','Closed time','Location','Duration','Max Lanes Closed']

I495 = []
I495_con = []
I66 = []
I66_con =[]
VA7 = []
VA7_con = []

dataSet1 = pd.read_csv(data_dir1,index_col = 0)
dataSet2 = pd.read_csv(data_dir2,index_col = 0)
print(dataSet1.info())


for i in range(len(dataSet1['Location'])):
    if 'I-495N north' in dataSet1['Location'][i] or 'I-495S south' in dataSet1['Location'][i]:
        I495.append(dataSet1.iloc[i].values.tolist())
    elif 'I-66W west' in dataSet1['Location'][i] or 'I-66E east' in dataSet1['Location'][i]:
        I66.append(dataSet1.iloc[i].values.tolist())
    elif 'VA-7E east' in dataSet1['Location'][i] or 'VA-7W west' in dataSet1['Location'][i]:
        VA7.append(dataSet1.iloc[i].values.tolist())

for i in range(len(dataSet2['Location'])):
    if 'I-495N north' in dataSet2['Location'][i] or 'I-495S south' in dataSet2['Location'][i]:
        I495_con.append(dataSet2.iloc[i].values.tolist())
    elif 'I-66W west' in dataSet2['Location'][i] or 'I-66E east' in dataSet2['Location'][i]:
        I66_con.append(dataSet2.iloc[i].values.tolist())
    elif 'VA-7E east' in dataSet2['Location'][i] or 'VA-7W west' in dataSet2['Location'][i]:
        VA7_con.append(dataSet2.iloc[i].values.tolist())

dataSet1['Start time'] = pd.to_datetime(dataSet1['Start time'])
dataSet2['Start time'] = pd.to_datetime(dataSet2['Start time'])

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

count_I66 = pd.value_counts(I66['Start time'].dt.day,sort = False)
count_I66 = pd.DataFrame({'date':np.unique(I66['Start time'].dt.day),'Count':count_I66})
count_I495 = pd.value_counts(I495['Start time'].dt.day,sort = False)
count_I495 = pd.DataFrame({'date':np.unique(I495['Start time'].dt.day),'Count':count_I495})
count_VA7 = pd.value_counts(VA7['Start time'].dt.day,sort = False)
count_VA7 = pd.DataFrame({'date':np.unique(VA7['Start time'].dt.day),'Count':count_VA7})

print(count_VA7)

count_I66_con = pd.value_counts(I66_con['Start time'].dt.day,sort = False)
count_I66_con = pd.DataFrame({'date':np.unique(I66_con['Start time'].dt.day),'Count':count_I66_con})
count_I495_con = pd.value_counts(I495_con['Start time'].dt.day,sort = False)
count_I495_con = pd.DataFrame({'date':np.unique(I495_con['Start time'].dt.day),'Count':count_I495_con})
count_VA7_con = pd.value_counts(VA7_con['Start time'].dt.day,sort = False)
count_VA7_con = pd.DataFrame({'date':np.unique(VA7_con['Start time'].dt.day),'Count':count_VA7_con})

con = pd.value_counts(dataSet2['Start time'].dt.day,sort = False)
count = pd.DataFrame({'date':np.unique(dataSet2['Start time'].dt.day),'Count':con})

plt.plot(count_VA7_con.date,
         count_VA7_con.Count,
         linestyle = '-',
         linewidth = 2,
         color ='steelblue',
         marker = 'o',
         markersize = 3,
         markeredgecolor = 'black',
         label = 'Constuction'
         )

plt.plot(count_I66.date,
         count_I66.Count,
         linestyle = '--',
         linewidth = 1,
         color ='blue',
         label = 'I66'
         )

plt.plot(count_I495.date,
         count_I495.Count,
         linestyle = '--',
         linewidth = 1,
         color ='indianred',
         label = 'I495'
         )

plt.plot(count_VA7.date,
         count_VA7.Count,
         linestyle = '--',
         linewidth = 1,
         marker='o',
         markersize=3,
         markeredgecolor='grey',
         color ='green',
         label = 'VA7'
         )

plt.ylabel = 'Count each day'
plt.xlabel = 'date'
plt.legend()
plt.show()