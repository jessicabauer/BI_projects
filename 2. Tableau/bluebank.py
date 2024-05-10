# -*- coding: utf-8 -*-
"""
Created on Mon May  6 09:52:25 2024

@author: admin
"""

import json 
import pandas as pd 
import numpy as np
import matplotlib .pyplot as plt

# METHOD-1 TO READ JSON DATA
json_file = open('loan_data_json.json')
data = json.load(json_file)

# METHOD-2 TO READ JSON DATA
'''with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    print(data)'''
    
'''

#WORKING WITH LISTS

lists = ['apple', 'banana', 'pear', 'pear']
# INDEX = 0/1/2/3

# APPEND TO A LIST
lists.append('cherry')
print(lists)

# INSERT ITEM INTO A SPECIFIC POSITION
lists.insert(1, 'grape')
print(lists)

# REMOVE ITEMS IN A LIST
lists.remove('pear')


# REMOVE LAST ITEM IN A LIST
lists.pop()

#JSON - WORKING WITH DICTIONARIES
mydict = {
    'name' : 'Jessica',
    'location' : 'Rolante',
    'favcolor': 'Red',
    'luckynumber': 7
    }

# ACCESS OTHER KEYS
color = mydict['favcolor']
print(color)

# TO GET A LIST OF KEYS
mydict.keys()

# TO GET A LIST OF VALUES
mydict.values()

# TO GET A LIST OF ITEMS
mydict.items()

# TO GET A NEW KEY/VARIABLE
mydict['gender']= 'female'
print (mydict) '''

# TRANFORM TO DATAFRAME
loandata = pd.DataFrame(data)

# Finding unique values for the PURPOSE column -CATEGORIAS DE VALORES QUE EXISTEM
loandata['purpose'].unique()

# DESCRIBE THE DATA
loandata.describe()

# DESCRIBE THE DATA FOR A SPECIFIC COLUMN
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

# Working with arrays - 1D ARRAY
arr = np.array([1, 2, 3, 4])

#0D Array
arr = np.array([43])

#2D Array
arr = np.array([ [1,2,3] , [4,5,6]] )

# WORKING WITH IF statements
a = 10
b = 500
c = 1000

if b > a: 
    print ('B is greater than a')

if b > a and b < c: 
    print('B is greater than A, but less than C')

# What if a condition IS NOT MET?

a =40
b =500
c =20

if b > a and b < c: 
    print('B is greater than A, but less than C')
else:
    print('No conditions met')

# Another condition different metrics

a = 40
b = 500
c = 30

if b > a and b < c:
    print('B is greater than A, but less than C')
elif b > a and b > c:
    print ('B is greater than A and C')
else: 
    print ('No conditions met')
    
    
# FICO STORE

fico = 700

# fico >= 300 and < 400: 'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent'


if fico >= 300 and fico < 400:
    ficocat = 'Very poor'
elif fico >=400 and fico < 600:
    ficocat = 'Poor'
elif fico >=601 and fico < 660:
    ficocat = 'Fair'
elif fico >=660 and fico <780:
    ficocat = 'Good'
elif fico >=780:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print (ficocat)


# LOOPS

fruits = ['apple', 'pear', 'banana']
for x in fruits:
    print (x)
    y = x + 'fruit'
    print (y)
    
for x in range (0,3):
    y = fruits[x] + ' for sale'
    print(y)
    
  # Applying for loops to loan data
  
  # Using first 10
  
  
  
lenght = len(loandata)
ficocat = []
for x in range (0,lenght):
      category = loandata['fico'][x]
      
      try:
          
          if category >= 300 and category < 400:
              cat = 'Very poor'
          elif category >=400 and category < 600:
              cat = 'Poor'
          elif category >=601 and category < 660:
              cat = 'Fair'
          elif category >=660 and category < 700:       
              cat = 'Good'
          elif category >700: 
              cat = 'Excellent'
          else:
              cat = 'Unknown'
      except:
            cat = 'Error - Unknown'
                  
      ficocat.append(cat) # para não sobrescrever
    
ficocat = pd.Series(ficocat)  
loandata['fico.category'] = ficocat
    
''' WHILE LOOPS
i=1
while i<=10:
    print (i)
    i= i+1 '''
    
  
#df.loc as conditional statements
# df.loc[df[columnname] condition, newcolumname] = 'value if the condition is met'

# For interest rates a new column is wanted. rate>0.12 then high, else low


loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

    
  # Number of loans/ rows by fico.category
  # SIZE - Count the number of rows
catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.3)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'green', width = 0.3)
plt.show()
  
# SCATTER PLOTS  - GRAFICO DE DISPERSÃO

# DTI - DEBTH INCOME RATIO
ypoint = loandata['annualincome'] 
xpoint = loandata['dti']  
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()  
    
  
 # WRITING TO CSV
   
#loandata.to_csv('loan_cleaned.', index = True)
loandata.to_parquet('loan_cleaned.parquet')
  
    
  
    
  
    
  
  
    
  
    
  
    
  
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    