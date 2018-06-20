# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 17:34:51 2018

@author: chris
"""

import pandas as pd
import os


def answer_one():
    summer_golds = df['Gold']
    summer_golds_sorted=summer_golds.sort_values(ascending = False)
    return summer_golds_sorted.index[0]

def answer_two():
    summer_golds = df['Gold']
    winter_golds = df['Gold.1']
    diff_golds = abs(summer_golds - winter_golds)
    diff_golds_sorted = diff_golds.sort_values(ascending = False)
    return diff_golds_sorted.index[0]

def answer_three():
    df['Sum of Golds']=df['Gold']+df['Gold.1']
    only_gold = df.where(df['Sum of Golds'] > 0)
    only_gold = only_gold.dropna()
    summer_golds = only_gold['Gold']
    winter_golds = only_gold['Gold.1']
    diff_golds = (summer_golds - winter_golds)/only_gold['Sum of Golds']
    diff_golds_sorted = diff_golds.sort_values(ascending = False)
    return diff_golds_sorted.index[0]

def answer_four():
    Points = 3*df['Gold.2']+2*df['Silver.2']+1*df['Bronze.2']
    return Points


headPATH, tailPATH = os.path.split(os.getcwd())
dataPATH = os.path.join(headPATH,'course1_downloads')
filename = os.path.join(dataPATH,'olympics.csv')


df = pd.read_csv(filename, index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

# Q1: Which country has won the most gold medals in summer games?
an1 = answer_one()

# Q2: Which country had the biggest difference between their summer 
#     and winter gold medal counts?
an2 = answer_two()

# Q3: Which country has the biggest difference between their summer gold medal
#    counts and winter gold medal counts relative to their total gold medal count?
an3 = answer_three()

# Q4: Write a function that creates a Series called "Points" which is a weighted 
#     value where each gold medal (Gold.2) counts for 3 points, silver medals 
#    (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. The 
#    function should return only the column (a Series object) which you created.
an4 = answer_four()



