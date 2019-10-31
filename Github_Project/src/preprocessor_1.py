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

I495_con = []
I66_con = []
VA7_con = []

for i in range(len(dataSet2)):
    if dataSet2['Duration'].iloc[i] >= 200:
        if 'I-495N north' in dataSet2['Location'].iloc[i] or 'I-495S south' in dataSet2['Location'].iloc[i]:
            I495_con.append(dataSet2.iloc[i].values.tolist())
        elif 'I-66W west' in dataSet2['Location'].iloc[i] or 'I-66E east' in dataSet2['Location'].iloc[i]:
            I66_con.append(dataSet2.iloc[i].values.tolist())
        elif 'VA-7E east' in dataSet2['Location'].iloc[i] or 'VA-7W west' in dataSet2['Location'].iloc[i]:
            VA7_con.append(dataSet2.iloc[i].values.tolist())

# I495_con = pd.DataFrame(I495_con, columns = index_name)
# I66_con = pd.DataFrame(I66_con, columns = index_name)
# VA7_con = pd.DataFrame(VA7_con, columns = index_name)

example_con = dataSet2.iloc[20:30]

example_con = pd.DataFrame(example_con,columns = index_name)

print(example_con)

dataSet1['Start time'] = pd.to_datetime(dataSet1['Start time'])
dataSet1['Closed time'] = pd.to_datetime(dataSet1['Closed time'])
example_con['Start time'] = pd.to_datetime(example_con['Start time'])
example_con['Closed time'] = pd.to_datetime(example_con['Closed time'])
I495 = []
I66 = []
VA7 = []
Total = []
for x in range(len(example_con)):
    I495_count = 0
    I66_count = 0
    VA7_count = 0
    for y in range(len(dataSet1)):
        if 'I-495N north' in dataSet1['Location'].iloc[y] or 'I-495S south' in dataSet1['Location'].iloc[y]:
            start = (example_con['Start time'].iloc[x] - dataSet1['Start time'].iloc[y]).days
            end = (example_con['Closed time'].iloc[x] - dataSet1['Start time'].iloc[y]).days
            if int(start) < 0 and int(end) >= 0:
                print(dataSet1['Start time'].iloc[y])
                I495_count += 1
        elif 'I-66W west' in dataSet1['Location'].iloc[y] or 'I-66E east' in dataSet1['Location'].iloc[y]:
            start = (example_con['Start time'].iloc[x] - dataSet1['Start time'].iloc[y]).days
            end = (example_con['Closed time'].iloc[x] - dataSet1['Start time'].iloc[y]).days
            if int(start) < 0 and int(end) >= 0:
                print(dataSet1['Start time'].iloc[y])
                I66_count += 1
        elif 'VA-7E east' in dataSet1['Location'].iloc[y] or 'VA-7W west' in dataSet1['Location'].iloc[y]:
            start = (example_con['Start time'].iloc[x] - dataSet1['Start time'].iloc[y]).days
            end = (example_con['Closed time'].iloc[x] - dataSet1['Start time'].iloc[y]).days
            if int(start) < 0 and int(end) >= 0:
                print(dataSet1['Start time'].iloc[y])
                VA7_count += 1
    I66.append(I66_count)
    I495.append(I495_count)
    VA7.append(VA7_count)
    Total.append(I66_count+I495_count+VA7_count)
    print(I495_count)
    print(I66_count)
    print(VA7_count)
    print('-------')

print(I495)
print(I66)
print(VA7)


list1 = ['case1','case2','case3','case4','case5','case6','case7','case8','case9','case10']

x = range(len(list1))
plt.bar(x, I495, width=0.1,label = 'I495')
plt.bar([i + 0.1 for i in x], I66, width=0.1,label = 'I66')
plt.bar([i + 0.2 for i in x], VA7, width=0.1,label = 'VA7')
plt.bar([i + 0.3 for i in x], Total, width=0.1,label = 'Total')
plt.legend()
plt.show()