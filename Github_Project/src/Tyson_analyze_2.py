import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

data_dir = '/Users/yuanjielu/Desktop/CEIE Project/Old_dataSet/1-6_col_new.csv'
data_dir1 = '/Users/yuanjielu/Desktop/CEIE Project/Old_dataSet/1-6_con_new.csv'
index_name = ['Standardized Type','Start time','Closed time','Location','Duration','Max Lanes Closed']

dataSet1 = pd.read_csv(data_dir,index_col = 0)
dataSet2 = pd.read_csv(data_dir1,index_col = 0)

dataSet1['Start time'] = pd.to_datetime(dataSet1['Start time'])
dataSet1['Closed time'] = pd.to_datetime(dataSet1['Closed time'])
dataSet2['Start time'] = pd.to_datetime(dataSet2['Start time'])
dataSet2['Closed time'] = pd.to_datetime(dataSet2['Closed time'])

# dataSet2.drop_duplicates(['Standardized Type','Start time'], inplace = True)

dataSet1['Max Lanes Closed'] = dataSet1['Max Lanes Closed'].fillna(0)
dataSet2['Max Lanes Closed'] = dataSet1['Max Lanes Closed'].fillna(0)
Duration_col = []
Duration_con = []
address_col = []
address_con = []
collision = []
construction = []

for i in range(len(dataSet1['Location'])):
    if dataSet1['Duration'].iloc[i] != 'Ends before it began':
        ts = dataSet1['Closed time'].iloc[i] - dataSet1['Start time'].iloc[i]
        days = float(ts.days * 24 * 60)
        ts = (float(ts.seconds) // 60)
        ts = days + ts

        if dataSet1['Standardized Type'].iloc[i] == 'Collision':
            if 'I-495N north' in dataSet1['Location'].iloc[i] or 'I-495S south' in dataSet1['Location'].iloc[i]:
                c = ""

                for x in dataSet1['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break

                if int(c[3:5]) > 40 and int(c[3:5]) < 50:
                    collision.append(dataSet1.iloc[i].values.tolist())
                    address_col.append('I-495')
                    if ts <= 30:
                        Duration_col.append('Level_1')
                    elif ts > 30 and ts <= 60:
                        Duration_col.append('Level_2')
                    elif ts > 60 and ts <= 120:
                        Duration_col.append('Level_3')
                    elif ts > 120 and ts <= 240:
                        Duration_col.append('Level_4')
                    elif ts > 240:
                        Duration_col.append('Level_5')
            elif 'I-66W west' in dataSet1['Location'].iloc[i] or 'I-66E east' in dataSet1['Location'].iloc[i]:
                c = ""
                for x in dataSet1['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if len(c) != 2:
                    if int(c[2:]) > 60 and int(c[2:]) < 70:
                        collision.append(dataSet1.iloc[i].values.tolist())
                        address_col.append('I-66')
                        if ts <= 30:
                            Duration_col.append('Level_1')
                        elif ts > 30 and ts <= 60:
                            Duration_col.append('Level_2')
                        elif ts > 60 and ts <= 120:
                            Duration_col.append('Level_3')
                        elif ts > 120 and ts <= 240:
                            Duration_col.append('Level_4')
                        elif ts > 240 :
                            Duration_col.append('Level_5')

            elif 'VA-123N north' in dataSet1['Location'].iloc[i] or 'VA-123S south' in dataSet1['Location'].iloc[i]:
                c = ""
                for x in dataSet1['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if len(c) != 3:
                    if int(c[3:]) > 16 and int(c[3:]) < 26:
                        collision.append(dataSet1.iloc[i].values.tolist())
                        address_col.append('Other')
                        if ts <= 30:
                            Duration_col.append('Level_1')
                        elif ts > 30 and ts <= 60:
                            Duration_col.append('Level_2')
                        elif ts > 60 and ts <= 120:
                            Duration_col.append('Level_3')
                        elif ts > 120 and ts <= 240:
                            Duration_col.append('Level_4')
                        elif ts > 240:
                            Duration_col.append('Level_5')
            elif 'VA-7E east' in dataSet1['Location'].iloc[i] or 'VA-7W west' in dataSet1['Location'].iloc[i]:
                c = ""
                for x in dataSet1['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if int(c[1:]) > 40 and int(c[1:]) < 90:
                    collision.append(dataSet1.iloc[i].values.tolist())
                    address_col.append('Other')
                    if ts <= 30:
                        Duration_col.append('Level_1')
                    elif ts > 30 and ts <= 60:
                        Duration_col.append('Level_2')
                    elif ts > 60 and ts <= 120:
                        Duration_col.append('Level_3')
                    elif ts > 120 and ts <= 240:
                        Duration_col.append('Level_4')
                    elif ts > 240:
                        Duration_col.append('Level_5')
for i in range(len(dataSet2['Location'])):
    if dataSet2['Duration'].iloc[i] != 'Ends before it began':
        ts = dataSet2['Closed time'].iloc[i] - dataSet2['Start time'].iloc[i]
        days = float(ts.days * 24 * 60)
        ts = (float(ts.seconds) // 60)
        ts = days + ts
        if ts >= 30 and ts <= 3000:
            if 'I-495N north' in dataSet2['Location'].iloc[i] or 'I-495S south' in dataSet2['Location'].iloc[i]:
                c = ""
                for x in dataSet2['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if int(c[3:5]) > 40 and int(c[3:5]) < 50:
                    construction.append(dataSet2.iloc[i].values.tolist())
                    Duration_con.append(ts)
                    address_con.append('I-495')
            elif 'I-66W west' in dataSet2['Location'].iloc[i] or 'I-66E east' in dataSet2['Location'].iloc[i]:
                c = ""
                for x in dataSet2['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if len(c) != 2:
                    if int(c[2:]) > 60 and int(c[2:]) < 70:
                        construction.append(dataSet2.iloc[i].values.tolist())
                        Duration_con.append(ts)
                        address_con.append('I-66')

            elif 'VA-123N north' in dataSet2['Location'].iloc[i] or 'VA-123S south' in dataSet2['Location'].iloc[i]:
                c = ""
                for x in dataSet2['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if len(c) != 3:
                    if int(c[3:]) > 16 and int(c[3:]) < 26:
                        construction.append(dataSet2.iloc[i].values.tolist())
                        Duration_con.append(ts)
                        address_con.append('Other')

            elif 'VA-7E east' in dataSet2['Location'].iloc[i] or 'VA-7W west' in dataSet2['Location'].iloc[i]:
                c = ""
                for x in dataSet2['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if int(c[1:]) > 40 and int(c[1:]) < 70:
                    construction.append(dataSet2.iloc[i].values.tolist())
                    Duration_con.append(ts)
                    address_con.append('Other')

collision = pd.DataFrame(collision, columns = index_name)
collision['Duration'] = Duration_col
collision['Location'] = address_col

print(collision)

construction = pd.DataFrame(construction, columns = index_name)
construction['Duration'] = Duration_con
construction['Location'] = address_con

print(construction)

collision_sort = []
construction_sort = []

for x in range(len(collision)):
    if 'I-495' in collision['Location'].iloc[x]:
        collision_sort.append(collision.iloc[x].values.tolist())
for y in range(len(collision)):
    if 'I-66' in collision['Location'].iloc[y]:
        collision_sort.append(collision.iloc[y].values.tolist())
for z in range(len(collision)):
    if 'Other' in collision['Location'].iloc[z]:
        collision_sort.append(collision.iloc[z].values.tolist())

for x in range(len(construction)):
    if 'I-495' in construction['Location'].iloc[x]:
        construction_sort.append(construction.iloc[x].values.tolist())
for y in range(len(construction)):
    if 'I-66' in construction['Location'].iloc[y]:
        construction_sort.append(construction.iloc[y].values.tolist())

for i in range(len(construction)):
    if 'Other' in construction['Location'].iloc[i]:
        construction_sort.append(construction.iloc[i].values.tolist())

collision_sort = pd.DataFrame(collision_sort, columns = index_name)
construction_sort = pd.DataFrame(construction_sort, columns = index_name)

print(collision_sort['Location'])
print(construction_sort['Location'])

construction_sort = construction_sort.sort_values('Duration', ascending=False).drop_duplicates(['Start time','Standardized Type','Location']).sort_index().reset_index(drop=True)
target_dir = '/Users/yuanjielu/Desktop/CEIE Project/TysonDataset/'

print(collision.info())
print(construction.info())
collision_sort.to_csv(target_dir + '1-6_col_1.csv')
construction_sort.to_csv(target_dir + '1-6_con_1.csv')

