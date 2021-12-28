

import os
import numpy as np
import pandas as pd
#from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.interactive(False)
#------------------------------------------------------------------------------
os.chdir(r'/Users/laith/Desktop/python lessons/Projects/Project2')
os.getcwd()
#------------------------------------------------------------------------------
# Read a Data Frame from the csv file:
data=pd.read_csv("IBM_Employee_Attrition.csv", na_values=' ', 
                    usecols=['EmployeeNumber', 'Attrition','Age', 'Gender' , 
                             'Department', 'DistanceFromHome', 'Education', 
                             'EducationField', 'HourlyRate', 'JobLevel', 'JobRole',
                             'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome',
                             'NumCompaniesWorked', 'PerformanceRating', 'TotalWorkingYears',
                             'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole'
                             ])
# Data Description:
data.shape
data.ndim
data.size
data.head()
missing=data.isnull().sum() # no missing values
print(missing)
data.describe()
data.dtypes
#------------------------------------------------------------------------------
# The number of attrited and not attrited employees: 

attrited = data.groupby(['Attrition']).count()

x = list(attrited['Age'])
x
#solution 2

attr_count = data['Attrition'].value_counts()
print(attr_count)

no_count=attr_count[0]
yes_count=attr_count[1]


#------------------------------------------------------------------------------
# Pie chart of Yes and No Attrition:




values = x

colors = ['b', 'g']

labels = ['Attrited','NotAttrited']

explode = (0.2, 0)

plt.pie(values, colors=colors, labels= values,autopct='%1.1f%%',explode=explode,counterclock=False, shadow=True)

plt.title('Attribited')

plt.legend(labels,loc=3)

plt.show()


#------------------------------------------------------------------------------
# Create new dataframe 'y_attr' to get all of attrited employees:

y_attr = data[data['Attrition']=="Yes"]
y_attr.shape
# Create new dataframe 'n_attr' to get all of not attrited employees:

x_attr = data[data['Attrition']=="No"]



#------------------------------------------------------------------------------



z_attr = data['Age'][data['Attrition']=="Yes"]
len(z_attr)
 

#--------------------------- BAR GRAPH


data['Education'].unique()

avg = data.groupby(['Education'])['MonthlyIncome'].mean()
type(avg)

value = list(avg)
value

labels = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5"]

pos = [0,1,2,3, 4]

plt.bar(pos,value ,color='lightskyblue',edgecolor='black')

plt.xticks(pos, labels)

plt.show()



#--------------------------- JOB ROLE and MONTHLY INCOME

avg = data.groupby(['JobRole'])['MonthlyIncome'].mean()

avg




#---------------------------- PIE CHART ON JOB ROLE and MONTHLY INCOME







#---------------------------- JOB ROLE and ATTRITION

job_attrition = data.groupby(['JobRole','Attrition'])['Age'].count()
print(job_attrition)



#----------------------------- PIE CHART ON JOB ROLE and ATTRITION




#------------------------------- Department and ATTRITION
dep_attrition = data.groupby(['Department','Attrition'])['Age'].count()
dep_attrition

#------------------------------- BAR GRAPH ON DEPARTMENT AND ATTRITION

value = list(dep_attrition)
value
 
labels = ["HRno", "HRyes", "RDno", "RDyes", "Sno", "Syes"]

pos = [0,1,2,3, 4, 5]

plt.bar(pos,value ,color='lightskyblue',edgecolor='black')

plt.xticks(pos, labels)

plt.show()


