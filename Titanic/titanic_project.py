

import os


os.getcwd()
os.chdir(r"/Users/laith/Desktop/python lessons/Projects") 

import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
plt.interactive(False)#interactive mode is off, you have to call plt.show() explicitly to pop up figure window.

#raw data analyze
titanic = pd.read_csv('titanic.csv')

type(titanic)
titanic.shape

titanic.ndim #number of dimension
titanic.size

titanic.dtypes
titanic["PassengerId"].dtype

titanic['Age'].dtype

titanic.info()


titanic.columns

titanic.head()

titanic.Age.describe()

#''''''''''''''''''
#create cleandata dataframe

cleandata = titanic[(titanic['Age'].notnull())&(titanic['Embarked'].notnull())] 
#remove the null rows with in columns "age"&"Embarcked"
cleandata.shape

cleandata.info()


#'''''''''''''
#gender by if survived
total_survived= cleandata['Survived'].sum()
total_survived


survive = cleandata.groupby(['Sex','Survived']).count()


survive.head()

survive.columns
type(survive)

# gender survive bar chart
sexsur=['FemaleNot','FemaleYes','MaleNot','MaleYes']

pos=np.arange(len(survive['PassengerId'])) #doesnt matter which coloumn

Count=survive['Age']

plt.bar(pos,Count,color='lightskyblue',edgecolor='black')

plt.xticks(pos, sexsur)

plt.xlabel('sexsur', fontsize=16)

plt.ylabel('Count', fontsize=16)

plt.title('Barchart - Survive by Gender',fontsize=20)

plt.show()



#male survive pie chart

values = [survive.ix[2,'Fare'],survive.ix[3,'Fare']]

colors = ['b', 'g']

labels = ['MaleNot','MaleYes']

explode = (0.2, 0)

plt.pie(values, colors=colors, labels= values,autopct='%1.1f%%',explode=explode,counterclock=False, shadow=True)

plt.title('Male Survive Rate')

plt.legend(labels,loc=3)

plt.show()

#frmale survive pie chart
values = [survive.ix[0,'Fare'],survive.ix[1,'Fare']]
colors = ['r', 'y',]
labels = ['FemaleNot','FemaleYes']
explode = (0.1, 0)
plt.pie(values, colors=colors, labels= values,autopct='%1.1f%%',explode=explode,counterclock=False, shadow=True)
plt.title('Female Survive Rate')
plt.legend(labels,loc=3)
plt.show()


#groupby shipclass to account the survive


shipclass=cleandata.groupby(['Pclass','Survived'])['Age'].count()

Ashipclass=np.array(shipclass)

sclass=['1','2','3']

ifalive=['Pass','Alive']

pos = np.arange(3)
pos
bar_width = 0.35

c=[0,2,4]

d=[1,3,5]

notsurvive=Ashipclass[c]

yessurvive=Ashipclass[d]

plt.bar(pos,notsurvive,bar_width,color='blue',edgecolor='black')

plt.bar(pos+bar_width,yessurvive,bar_width,color='pink',edgecolor='black')

plt.xticks(pos, sclass)

plt.xlabel('Room Class', fontsize=16)

plt.ylabel('Count of Survive', fontsize=16)

plt.title('Barchart - survive Count by Class',fontsize=18)

plt.legend(ifalive,loc=2)

plt.show()


#Mean fare of each class
classfare=cleandata.groupby('Pclass')['Fare'].mean()
Aclassfare=np.array(classfare)

#average age of the death and alive 
cleandata.groupby('Survived')['Age'].mean()
alldead=cleandata[cleandata['Survived']==0]
alldead.Age.describe()
Aalldead=np.array(alldead['Age'])
allalive=cleandata[cleandata['Survived']==1]
allalive.Age.describe()
Aallalive=np.array(allalive['Age'])
box_plot_data=[Aalldead,Aallalive]
plt.boxplot(box_plot_data,labels=['Alldead','Allalive'])
plt.show()


#count the number of different group
child=cleandata[cleandata['Age']<18]
child.head()
child.Age.count()
child_alive=child[child['Survived']==1]['Age'].count()
Child_dead=child.Age.count()-child_alive
young=cleandata[(cleandata['Age']>=18) & (cleandata['Age']<35)]
young.Age.count()
young_alive=young[young['Survived']==1]['Age'].count()
young_dead=young.Age.count()-young_alive
adult=cleandata[(cleandata['Age']>=35) & (cleandata['Age']<60)]
adult.Age.count()
adult_alive=adult[adult['Survived']==1]['Age'].count()
adult_dead=adult.Age.count()-adult_alive
old=cleandata[cleandata['Age']>=60]
old.Age.count()
old_alive=old[old['Survived']==1]['Age'].count()
old_dead=old.Age.count()-old_alive

#pie chart of the 
values = [child_alive, Child_dead, young_alive, young_dead,adult_alive,adult_dead,old_alive,old_dead]
colors = ['b', 'g', 'r', 'c' ,'m', 'y','b','r']
labels = ['child_alive', 'Child_dead', 'young_alive', 'young_dead','adult_alive','adult_dead','old_alive','old_dead']
explode = (0, 0, 0,0.2,0,0,0,0)
plt.pie(values, colors=colors, labels= labels,explode=explode,autopct='%1.1f%%',counterclock=False, shadow=True)
plt.title('Age Survive Percentage')
plt.legend(labels,loc=3)
plt.show()


#average price for each pclass
cleandata.groupby('Pclass')['Fare'].mean()

#numbers from each port
cleandata.groupby('Embarked')['Fare'].count()


#Is there any link between port and Pclass?
#C = Cherbourg; Q = Queenstown; S = Southampton
cleandata.groupby(['Embarked','Pclass'])['Fare'].count()



#Is there any link between port and Survive?
cleandata.groupby(['Embarked','Survived'])['Fare'].count()