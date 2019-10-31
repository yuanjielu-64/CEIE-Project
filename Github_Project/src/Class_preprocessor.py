import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_dir1 = '/Users/yuanjielu/Desktop/CEIE Project/temp/1.csv'
data_dir2 = '/Users/yuanjielu/Desktop/CEIE Project/temp/2.csv'
data_dir3 = '/Users/yuanjielu/Desktop/CEIE Project/temp/3.csv'
data_dir4 = '/Users/yuanjielu/Desktop/CEIE Project/temp/4.csv'
data_dir5 = '/Users/yuanjielu/Desktop/CEIE Project/temp/5.csv'
data_dir6 = '/Users/yuanjielu/Desktop/CEIE Project/temp/6.csv'

index_name = ['Standardized Type','Start time','Closed time','Location','Duration','Max Lanes Closed']

dataSet1 = pd.read_csv(data_dir2,index_col = 0)
# dataSet2 = pd.read_csv(data_dir2,index_col = 0)
# dataSet3 = pd.read_csv(data_dir3,index_col = 0)
# dataSet4 = pd.read_csv(data_dir4,index_col = 0)
# dataSet5 = pd.read_csv(data_dir5,index_col = 0)`
# dataSet6 = pd.read_csv(data_dir6,index_col = 0)

dataSet1['Start time'] = pd.to_datetime(dataSet1['Start time'])
dataSet1['Closed time'] = pd.to_datetime(dataSet1['Closed time'])
# print(dataSet1['Start time'])

dataSet1.drop_duplicates(['Standardized Type','Start time'],inplace = True)

# print(dataSet1['Start time'].dt.day)
# print(dataSet1['Closed time'].dt.day)

collision = []
construction = []
Duration_col = []
Duration_con = []
I495 = []
I66 = []
VA7 = []

for i in range(len(dataSet1)):

    if dataSet1['Duration (Incident clearance time)'].iloc[i] != 'Ends before it began':
        ts = dataSet1['Closed time'].iloc[i] - dataSet1['Start time'].iloc[i]
        ts = (int(ts.seconds) // 60)
        if ts >=30:
            if dataSet1['Standardized Type'].iloc[i] == 'Collision':
                if 'I-495N north' in dataSet1['Location'].iloc[i] or 'I-495S south' in dataSet1['Location'].iloc[i]:
                    c = ""
                    for x in dataSet1['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break

                    if int(c[3:5]) > 32 and int(c[3:5]) < 60:
                        collision.append(dataSet1.iloc[i].values.tolist())
                        Duration_col.append(ts)
                elif 'I-66W west' in dataSet1['Location'].iloc[i] or 'I-66E east' in dataSet1['Location'].iloc[i]:
                    c = ""
                    for x in dataSet1['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break
                    if len(c) != 2:
                        if int(c[2:]) > 51 and int(c[2:]) < 81:
                            collision.append(dataSet1.iloc[i].values.tolist())
                            Duration_col.append(ts)
                elif 'VA-7E east' in dataSet1['Location'].iloc[i] or 'VA-7W west' in dataSet1['Location'].iloc[i]:
                    c = ""
                    for x in dataSet1['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break
                    if int(c[1:]) > 40 and int(c[1:]) < 90:
                        collision.append(dataSet1.iloc[i].values.tolist())
                        Duration_col.append(ts)
            else:
                if 'I-495N north' in dataSet1['Location'].iloc[i] or 'I-495S south' in dataSet1['Location'].iloc[i]:
                    c = ""
                    for x in dataSet1['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break

                    if int(c[3:5]) > 32 and int(c[3:5]) < 60:
                        construction.append(dataSet1.iloc[i].values.tolist())
                        Duration_con.append(ts)
                elif 'I-66W west' in dataSet1['Location'].iloc[i] or 'I-66E east' in dataSet1['Location'].iloc[i]:
                    c = ""
                    for x in dataSet1['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break
                    if len(c) != 2:
                        if int(c[2:]) > 51 and int(c[2:]) < 81:
                            construction.append(dataSet1.iloc[i].values.tolist())
                            Duration_con.append(ts)
                elif 'VA-7E east' in dataSet1['Location'].iloc[i] or 'VA-7W west' in dataSet1['Location'].iloc[i]:
                    c = ""
                    for x in dataSet1['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break
                    if int(c[1:]) > 40 and int(c[1:]) < 60:
                        construction.append(dataSet1.iloc[i].values.tolist())
                        Duration_con.append(ts)

collision = pd.DataFrame(collision, columns = index_name)
collision['Duration'] = Duration_col

construction = pd.DataFrame(construction, columns = index_name)
construction['Duration'] = Duration_con

target_dir = '/Users/yuanjielu/Desktop/CEIE Project/wholeproject/'

collision.to_csv(target_dir + 'col2.csv')
construction.to_csv(target_dir + 'con2.csv')