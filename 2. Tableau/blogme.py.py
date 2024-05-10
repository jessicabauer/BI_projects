# -*- coding: utf-8 -*-
"""
Created on Tue May  7 08:44:53 2024

@author: admin
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# Reading excel ou xlsx files
data = pd.read_excel('articles.xlsx')

# Summary of the data
data.describe()
# Summary of the columns
data.info()

# Counting the number of articles per source
# Format of group by: df.groupby(['column_to_group'])['columns_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

# How much reactions do the articles get by publisher?
# number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# dropping a column =  AXIS = 1 referencia que estou excluindo uma coluna
data = data.drop('engagement_comment_plugin_count', axis=1)

# Function in python

def thisFunction():
    print('This is my First Function!')

thisFunction()

# This is a function with variables

# def aboutMe(name, surname, location):
#     print('This is '+ name+ ' My surname is ' + surname + 'I am from ' + location)
#     return name, surname, location

# a = aboutMe('Jéssica', 'Bauer', 'Rolante-RS')


# Using FOR loops in functions

# def favfood(food):
#     for x in food: # for every item in a food list'''
#         print ('Top food is ' +x)
    
    
# fastfood = ['burguers', 'pizza', 'pie']
# healthy = ['salad', 'water', 'fruit']

# favfood(healthy)
    
# Creating a keyword flag
keyword = 'crash'

# create a for loop to isolate each title row
# data['title'][0] - posição zero - Linha zero da coluna título

# lenght = len(data)
# keyword_flag = []
# for x in range (0,lenght):
#     heading = data['title'][x]
#     if keyword in heading: 
#         flag = 1
#     else:
#         flag = 0
#         keyword_flag.append(flag)

# Creating a fucntion

def keywordflag(keyword):
    lenght = len(data)
    keyword_flag = []
    for x in range (0,lenght):
        heading = data['title'][x]
        try:
            if keyword in heading: 
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
        
keywordflag = keywordflag("child")

# Creating a new column in data dataframe

data['keyword_flag'] = pd.Series(keywordflag)


# SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()
text = data['title'][16]
sent = sent_int.polarity_scores(text)

neg = sent ['neg']
pos = sent ['pos']
neu = sent ['neu']

# Adding a FOR loop to extract sentiment per title

title_neg_sentiment =[]
title_pos_sentiment =[]
title_neu_sentiment =[]

lenght = len(data)

for x in range (0, lenght):
    try:
        text = data ['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent ['neg']
        pos = sent ['pos']
        neu = sent ['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment 
data['title_pos_sentiment'] = title_pos_sentiment 
data['title_neu_sentiment'] = title_neu_sentiment 


data.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index = False)













