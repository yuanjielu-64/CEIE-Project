import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

data_dir = '/Users/yuanjielu/Desktop/CEIE Project/Peter/col.csv'
data_dir1 = '/Users/yuanjielu/Desktop/CEIE Project/Peter/con.csv'
index_name = ['Standardized Type','Start time','Closed time','Location','Duration','Max Lanes Closed']

dataSet1 = pd.read_csv(data_dir,index_col = 0)
dataSet2 = pd.read_csv(data_dir1,index_col = 0)

dataSet1['Start time'] = pd.to_datetime(dataSet1['Start time'])
dataSet1['Closed time'] = pd.to_datetime(dataSet1['Closed time'])
dataSet2['Start time'] = pd.to_datetime(dataSet2['Start time'])
dataSet2['Closed time'] = pd.to_datetime(dataSet2['Closed time'])

# dataSet1['Max Lanes Closed'] = dataSet1['Max Lanes Closed'].fillna(0)
# dataSet2['Max Lanes Closed'] = dataSet1['Max Lanes Closed'].fillna(0)
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
            if 'I-95N north' in dataSet1['Location'].iloc[i] or 'I-95S south' in dataSet1['Location'].iloc[i]:
                c = ""

                for x in dataSet1['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break

                if int(c[2:]) > 40 and int(c[2:]) < 60:
                    collision.append(dataSet1.iloc[i].values.tolist())
                    address_col.append('I-95')
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
            elif 'US-1N north' in dataSet1['Location'].iloc[i] or 'US-1S south' in dataSet1['Location'].iloc[i]:
                c = ""
                for x in dataSet1['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if len(c) != 1:
                    if int(c[1:]) > 65 and int(c[2:]) < 75:
                        collision.append(dataSet1.iloc[i].values.tolist())
                        address_col.append('US-1')
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

            elif 'I-295N north' in dataSet1['Location'].iloc[i] or 'I-295S south' in dataSet1['Location'].iloc[i]:
                c = ""
                for x in dataSet1['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if len(c) != 3:
                    if int(c[3:]) > 0 and int(c[3:]) < 12:
                        collision.append(dataSet1.iloc[i].values.tolist())
                        address_col.append('I-295')
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
            elif 'I-85N north' in dataSet1['Location'].iloc[i] or 'I-85S south' in dataSet1['Location'].iloc[i]:
                c = ""
                for x in dataSet1['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if len(c) != 2:
                    if int(c[2:]) >= 63:
                        collision.append(dataSet1.iloc[i].values.tolist())
                        address_col.append('I-85')
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
            elif 'US-460' in dataSet1['Location'].iloc[i]:
                c = ""
                for x in dataSet1['Location'].iloc[i]:
                    if x.isdigit():
                        c += x
                    if x == '.':
                        break
                if len(c) != 3:
                    if int(c[3:]) > 310 and int(c[3:]) < 350:
                        collision.append(dataSet1.iloc[i].values.tolist())
                        address_col.append('US-460')
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
        if ts.days != None:
            days = float(ts.days * 24 * 60)
            ts = (float(ts.seconds) // 60)
            ts = days + ts
            if ts >= 30 and ts <= 5000:
                if 'I-95N north' in dataSet2['Location'].iloc[i] or 'I-95S south' in dataSet2['Location'].iloc[i]:
                    c = ""
                    for x in dataSet2['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break
                    if int(c[2:]) > 40 and int(c[2:]) < 60:
                        construction.append(dataSet2.iloc[i].values.tolist())
                        Duration_con.append(ts)
                        address_con.append('I-95')
                elif 'US-1N north' in dataSet2['Location'].iloc[i] or 'US-1S south' in dataSet2['Location'].iloc[i]:
                    c = ""
                    for x in dataSet2['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break
                    if len(c) != 1:
                        if int(c[1:]) > 65 and int(c[2:]) < 75:
                            construction.append(dataSet2.iloc[i].values.tolist())
                            Duration_con.append(ts)
                            address_con.append('US-1')

                elif 'I-295N north' in dataSet2['Location'].iloc[i] or 'I-295S south' in dataSet2['Location'].iloc[i]:
                    c = ""
                    for x in dataSet2['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break
                    if len(c) != 3:
                        if int(c[3:]) > 0 and int(c[3:]) < 12:
                            construction.append(dataSet2.iloc[i].values.tolist())
                            Duration_con.append(ts)
                            address_con.append('I-295')
                elif 'I-85N north' in dataSet2['Location'].iloc[i] or 'I-85S south' in dataSet2['Location'].iloc[i]:
                    c = ""
                    for x in dataSet2['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break
                    if len(c) != 2:
                        if int(c[2:]) >= 63:
                            construction.append(dataSet2.iloc[i].values.tolist())
                            Duration_con.append(ts)
                            address_con.append('I-85')
                elif 'US-460' in dataSet2['Location'].iloc[i]:
                    c = ""
                    for x in dataSet2['Location'].iloc[i]:
                        if x.isdigit():
                            c += x
                        if x == '.':
                            break
                    if len(c) != 3:
                        if int(c[3:]) > 310 and int(c[3:]) < 350:
                            construction.append(dataSet2.iloc[i].values.tolist())
                            Duration_con.append(ts)
                            address_con.append('US-460')

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
    if 'I-95' in collision['Location'].iloc[x]:
        collision_sort.append(collision.iloc[x].values.tolist())
for y in range(len(collision)):
    if 'US-1' in collision['Location'].iloc[y]:
        collision_sort.append(collision.iloc[y].values.tolist())
for z in range(len(collision)):
    if 'I-295' in collision['Location'].iloc[z]:
        collision_sort.append(collision.iloc[z].values.tolist())
for z in range(len(collision)):
    if 'US-460' in collision['Location'].iloc[z]:
        collision_sort.append(collision.iloc[z].values.tolist())

for x in range(len(construction)):
    if 'I-95' in construction['Location'].iloc[x]:
        construction_sort.append(construction.iloc[x].values.tolist())
for y in range(len(construction)):
    if 'US-1' in construction['Location'].iloc[y]:
        construction_sort.append(construction.iloc[y].values.tolist())

for i in range(len(construction)):
    if 'I-295' in construction['Location'].iloc[i]:
        construction_sort.append(construction.iloc[i].values.tolist())

for i in range(len(construction)):
    if 'US-460' in construction['Location'].iloc[i]:
        construction_sort.append(construction.iloc[i].values.tolist())

collision_sort = pd.DataFrame(collision_sort, columns = index_name)
construction_sort = pd.DataFrame(construction_sort, columns = index_name)

print(collision_sort['Location'])
print(construction_sort['Location'])

# construction_sort.sort_values('Duration').drop_duplicates(['Standardized Type','Start time'], keep='last', inplace = True)
# construction_sort.groupby('Start time', group_keys=False).apply(lambda x: x.ix[x['Duration'].idxmax()])
construction_sort = construction_sort.sort_values('Duration', ascending=False).drop_duplicates(['Start time','Standardized Type','Location']).sort_index().reset_index(drop=True)

target_dir = '/Users/yuanjielu/Desktop/CEIE Project/Peter/'

print(collision.info())
print(construction.info())
collision_sort.to_csv(target_dir + 'col_1.csv')
construction_sort.to_csv(target_dir + 'con_1.csv')

