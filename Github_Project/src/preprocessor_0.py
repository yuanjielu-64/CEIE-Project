import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

data_dir = '/Users/yuanjielu/Desktop/CEIE Project/Old_dataSet/ritis-events(Jan-June).csv'
index_name = ['Standardized Type','Start time','Closed time','Location','Duration','Max Lanes Closed']

dataSet1 = pd.read_csv(data_dir,usecols = [1,3,4,5,7,10])

dataSet1['Start time'] = pd.to_datetime(dataSet1['Start time'])
dataSet1['Closed time'] = pd.to_datetime(dataSet1['Closed time'])
dataSet1.drop_duplicates(['Standardized Type','Start time'],inplace = True)

Duration_col = []
Duration_con = []
collision = []
construction = []

for i in range(len(dataSet1['Location'])):
    if dataSet1['Duration (Incident clearance time)'].iloc[i] != 'Ends before it began':
        ts = dataSet1['Closed time'].iloc[i] - dataSet1['Start time'].iloc[i]
        days = ts.days * 24 * 60
        ts = (int(ts.seconds) // 60)
        ts = days + ts
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

collision_sort = []
construction_sort = []
print(collision)
for x in range(len(collision)):
    if 'I-495N north' in collision['Location'].iloc[x] or 'I-495S south' in collision['Location'].iloc[x]:
        collision_sort.append(collision.iloc[x].values.tolist())
for y in range(len(collision)):
    if 'I-66W west' in collision['Location'].iloc[y] or 'I-66E east' in collision['Location'].iloc[y]:
        collision_sort.append(collision.iloc[y].values.tolist())
for z in range(len(collision)):
    if 'VA-7E east' in collision['Location'].iloc[z] or 'VA-7W west' in collision['Location'].iloc[z]:
        collision_sort.append(collision.iloc[z].values.tolist())

for x in range(len(construction)):
    if 'I-495N north' in construction['Location'].iloc[x] or 'I-495S south' in construction['Location'].iloc[x]:
        construction_sort.append(construction.iloc[x].values.tolist())
for y in range(len(construction)):
    if 'I-66W west' in construction['Location'].iloc[y] or 'I-66E east' in construction['Location'].iloc[y]:
        construction_sort.append(construction.iloc[y].values.tolist())
for z in range(len(construction)):
    if 'VA-7E east' in construction['Location'].iloc[z] or 'VA-7W west' in construction['Location'].iloc[z]:
        construction_sort.append(construction.iloc[z].values.tolist())

collision_sort = pd.DataFrame(collision_sort, columns = index_name)
construction_sort = pd.DataFrame(construction_sort, columns = index_name)
target_dir = '/Users/yuanjielu/Desktop/CEIE Project/wholeproject/'

# print(collision.info())
# print(construction.info())
# collision_sort.to_csv(target_dir + '1-6_col.csv')
# construction_sort.to_csv(target_dir + '1-6_con.csv')