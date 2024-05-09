# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:28:59 2024

@author: admin
"""
import pandas as pd

# file_name = pd.read_csv('file.csv') - Formato para ler arquivo CSV

# data= pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv', sep=';')

# SUMMARY OF THE DATA

data.info()

# Playing around with variables
''' var = 'Hello World'

#Array de itens
var = ['apple', 'pear', 'banana']

# Tupla utiliza () e é estática, não se pode mudar os valores
var = ('apple', 'pear', 'banana')

# 0,1,2,3,4,5,6,7,8,9,10 - ARRAY
var = range(0, 10)

# Dicionário
var = {'name': 'Jessica', 'Location': 'Brasil'}

#Lista de itens
var = {'apple', 'pear', 'banana'}

var = True  '''

# Working with calculations 

# Defining variables

CostPerItem= 11.73
SelllingPricePerItem= 21.11
NumberofItemsPurchased = 6

#Mathematical Operations on Tableau

# ProfitPerItem = 21.11 - 11.73

ProfitPerItem = SelllingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased *ProfitPerItem
SellingPricePerTransaction = SelllingPricePerItem * NumberofItemsPurchased
CostPerTransaction = CostPerItem *NumberofItemsPurchased

# CostPerTransaction column calculation
# Variable = dataframe ['column_name'] = FORMA MAIS LONGA
# Adding a new column to a dataframe
'''CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem *NumberofItemsPurchased'''


data['CostPerTransaction'] = CostPerTransaction

## FORMA MAIS SIMPLES
data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']


# Sales per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Proft Calculation = Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['ProfitPerTransaction'] = round(data['ProfitPerTransaction'], 2)

data['ProfitPerItem'] = round(data['ProfitPerItem'], 2)

#Markup = (Sales - Cost)/ Cost
data['markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/data['CostPerTransaction']

# data['markup'] = data['ProfitPerTransaction'])/data['CostPerTransaction']


## ROUND FUNCTION - MARK UP - ARREDONDAR NUMERO 2 CASAS
roundmarkup = round(data['markup'], 2)
data['markup'] = round(data['markup'], 2)

# Combing data fields
my_name = 'Jessica' + 'Bauer'
my_date = 'Day' + '-'+ 'Month' + '-'+ 'Year'


# my_date = data['Day']+ '-'  = NÃO VAI FUNCIONAR CONCATENAR STRING E INT

#Checking columns data type
print(data['Day'].dtype)

# Change columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
my_date = day + '-' + data['Month'] +'-'+year


data['date'] = my_date


# Using ILOC to view specific columns/rows

data.iloc[0]  #views the row with index = 0
data.iloc[0:3]  # views first 3 rows
data.iloc[-5]  # last 5 rows
data.head(5)  # Primeiras 5 linhas
data.iloc[:,2]  # :, = TODAS AS LINHAS    2 = COLUNA NUMERO 2
data.iloc[4,2]  # Linha 4 da coluna 2


# SPLIT to split the clients keywords field

#new_var = column.str.split('sep', expand =True)    expand =True - expande todos os itens


split_col = data['ClientKeywords'].str.split(',' , expand=True)

# Creating new columns for the split columns
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LenghtofContract'] = split_col[2]


# Using the REPLACE fuction
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LenghtofContract'] = data['LenghtofContract'].str.replace(']', '')


data['ClientAge'] = data['ClientAge'].str.replace("'", '')
data['ClientType'] = data['ClientType'].str.replace("'", '')
data['LenghtofContract'] = data['LenghtofContract'].str.replace("'", '')


# Using lowerfunction to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()
data['ItemDescription'] = data['ItemDescription'].str.title()


# MERGE FILES  NEW DATASET

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# MERGING FILES: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

# DROP COLUMNS FROM DATAFRAME

# df = df.drop ('columnname', axis = 1)

data = data.drop('ClientKeywords', axis=1)
data = data.drop('Day', axis=1)
data = data.drop(['Year', 'Month'], axis=1)


# EXPORT into CSV dataframe
data.to_csv('ValueInc_Cleaned.csv', index = False)









