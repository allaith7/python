#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:11:47 2019

@author: laith
"""

import os
os.chdir(r'/Users/laith/Desktop/python lessons/Projects/Fifa')

import pandas as pd
import numpy as np
#from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.interactive(False)





#-----select some useful columns from  the original dataset (because some columns are useless for analyis)
fifa=pd.read_csv('fifa_data.csv', na_values='NA', header=0,usecols=['Name','Age','Overall','Nationality','Club','Position','Value','Wage','Preferred Foot','Height','Weight'])

fifa['Height'] = fifa['Height'].str.replace("'", '.')

fifa['Weight'] = fifa['Weight'].str.replace("lbs", '')

fifa['Height']= fifa['Height'].str.replace("5.10", '5.93')
fifa['Height']= fifa['Height'].str.replace("5.11", '5.97')



#-----------------Creating File


fifa.to_csv('fifa_useful_data.csv', index=False) #creates new csv file with clean dataset


#-----Starting Point


fifa1 = pd.read_csv('fifa_useful_data.csv', na_values='NA', header=0)


type(fifa1)
fifa1.shape
fifa1.ndim
fifa1.head()

sorted_overall = fifa1.sort_values(by='Overall', ascending=False)

first_100 = sorted_overall.head(100)
first_100


Age = first_100['Age'].mean()
Age

#-------------

Age100 = first_100['Age']

type(Age100)

bp = plt.boxplot(Age100, patch_artist=True)

for x in bp['boxes']:
    x.set(color='red', linewidth=2)
    x.set(facecolor = 'green')

plt.show()

#------------ top player from each club

top_players = first_100.drop_duplicates(['Club'])
top_players



#----------------Correlation between height and weight


weight = first_100['Weight']
height = first_100['Height']
plt.scatter(height, weight)
plt.xlabel('height', fontsize=16)
plt.ylabel('weight', fontsize=16)

plt.title('Height vs Weight')


plt.show()


#------------------
first_100.info()



wage = first_100['Wage']
value = first_100['Value']
plt.scatter(value, wage)
plt.xlabel('value', fontsize=16)
plt.ylabel('wage', fontsize=16)

plt.title('wage vs value')


plt.show()
#---------------

pref_foot = first_100.groupby(['Preferred Foot'])['Age'].count()
pref_foot_avg = first_100.groupby(['Preferred Foot'])['Age'].mean()

pref_foot
pref_foot_avg


first_100.Club.value_counts()

len(first_100.Club.unique())

first_100.drop_duplicates(['Club'], keep='last')

#----------------

first_100.groupby(['Nationality'])['Age'].mean()

nat_avg = first_100.groupby(['Nationality'])['Age'].mean()

v = nat_avg.values


loc = np.argmax(v)


i = nat_avg.index

i[loc]


#--------------- HW - pie grpah of frequency count of players from my top 10 favorite clubs in "first_100" dataframe

















































