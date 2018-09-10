# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 16:00:44 2018

@author: chris
"""
# Data processing
import pandas as pd
import numpy as np
import json
from collections import Counter
from itertools import chain
from sklearn.feature_extraction.text import TfidfVectorizer
import re

# Data vizualizations
import random
import plotly
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 
init_notebook_mode(connected=True)
import plotly.offline as offline
import plotly.graph_objs as go
#
## Data Modeling
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.preprocessing import LabelEncoder
#from sklearn.linear_model import LogisticRegression
#from sklearn.svm import SVC
#from sklearn.ensemble import VotingClassifier
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import KFold
#from sklearn import model_selection 
#import warnings
#warnings.filterwarnings('ignore')

train_data = pd.read_json('train.json') # store as dataframe objects
test_data = pd.read_json('test.json')

train_data.info() #description of test data - 39774 x 3
train_data.head()

test_data.info() # description of test data - 9944 x 2

# How many different cuisines are included?
train_data['cuisine'].unique()   # 20 different cuisines => multi-class classification
cuisine_num = len(train_data['cuisine'].unique())

def random_colours(number_of_colors):
    '''
    Simple function for random colours generation.
    Input:
        number_of_colors - integer value indicating the number of colours which are going to be generated.
    Output:
        Color in the following format: ['#E86DA4'] .
    '''
    colors = []
    for i in range(number_of_colors):
        colors.append("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
    return colors


trace = go.Table(
                header=dict(values=['Cuisine','Number of recipes'],
                fill = dict(color=['#EABEB0']), 
                align = ['left'] * 5),
                cells=dict(values=[train_data.cuisine.value_counts().index,train_data.cuisine.value_counts()],
               align = ['left'] * 5))

layout = go.Layout(title='Number of recipes in each cuisine category',
                   titlefont = dict(size = 20),
                   width=500, height=650, 
                   paper_bgcolor =  'rgba(0,0,0,0)',
                   plot_bgcolor = 'rgba(0,0,0,0)',
                   autosize = False,
                   margin=dict(l=30,r=30,b=1,t=50,pad=1),
                   )
data = [trace]
fig = dict(data=data, layout=layout)
plot(fig)

#  Label distribution in percents
labelpercents = []
for i in train_data.cuisine.value_counts():
    percent = (i/sum(train_data.cuisine.value_counts()))*100
    percent = "%.2f" % percent
    percent = str(percent + '%')
    labelpercents.append(percent)
    
trace = go.Bar(
            x=train_data.cuisine.value_counts().values[::-1],
            y= [i for i in train_data.cuisine.value_counts().index][::-1],
            text =labelpercents[::-1],  textposition = 'outside', 
            orientation = 'h',marker = dict(color = random_colours(20)))
layout = go.Layout(title='Number of recipes in each cuisine category',
                   titlefont = dict(size = 25),
                   width=1000, height=450, 
                   plot_bgcolor = 'rgba(0,0,0,0)',
                   paper_bgcolor = 'rgba(255, 219, 227, 0.88)',
                   margin=dict(l=75,r=110,b=50,t=60),
                   )
data = [trace]
fig = dict(data=data, layout=layout)
plot(fig, filename='horizontal-bar')

# How many ingredients are there in a dish??
print('Maximum Number of Ingredients in a Dish: ',train_data['ingredients'].str.len().max())
print('Minimum Number of Ingredients in a Dish: ',train_data['ingredients'].str.len().min())

# Distribution of recipe length - it is right skewed, mode = 9 
trace = go.Histogram(
    x= train_data['ingredients'].str.len(),
    xbins=dict(start=0,end=90,size=1),
   marker=dict(color='#7CFDF0'),
    opacity=0.75)
data = [trace]
layout = go.Layout(
    title='Distribution of Recipe Length',
    xaxis=dict(title='Number of ingredients'),
    yaxis=dict(title='Count of recipes'),
    bargap=0.1,
    bargroupgap=0.2)

fig = go.Figure(data=data, layout=layout)
plot(fig)

# How many long and how many short recipes are there?
longrecipes = train_data[train_data['ingredients'].str.len() > 30]
print("It seems that {} recipes consist of more than 30 ingredients!".format(len(longrecipes)))

shortrecipes = train_data[train_data['ingredients'].str.len() <= 2]
print("It seems that {} recipes consist of less than or equal to 2 ingredients!".format(len(shortrecipes)))

# Boxplots
boxplotcolors = random_colours(21)
labels = [i for i in train_data.cuisine.value_counts().index][::-1]
data = []
for i in range(cuisine_num):
    trace = go.Box(
    y=train_data[train_data['cuisine'] == labels[i]]['ingredients'].str.len(), name = labels[i],
    marker = dict(color = boxplotcolors[i]))
    data.append(trace)
layout = go.Layout(
    title = "Recipe Length Distribution by cuisine")
fig = go.Figure(data=data,layout=layout)
plot(fig, filename = "Box Plot Styling Outliers")


# Find how many unique ingredients there are
allingredients = [] # this list stores all the ingredients in all recipes (with duplicates)
for item in train_data['ingredients']:
    for ingr in item:
        allingredients.append(ingr) 
        
# Count how many times each ingredient occurs
countingr = Counter()
for ingr in allingredients:
     countingr[ingr] += 1

print("The most commonly used ingredients (with counts) are:")
print("\n")
print(countingr.most_common(20))
print("\n")
print("The number of unique ingredients in our training sample is {}.".format(len(countingr)))

# Extract the first 20 most common ingredients in order to vizualize them for better understanding
mostcommon = countingr.most_common(20)
mostcommoningr = [i[0] for i in mostcommon]
mostcommoningr_count = [i[1] for i in mostcommon]

trace = go.Bar(
            x=mostcommoningr_count[::-1],
            y= mostcommoningr[::-1],
            orientation = 'h',marker = dict(color = random_colours(20),
))
layout = go.Layout(
    xaxis = dict(title= 'Number of occurences in all recipes (training sample)', ),
    yaxis = dict(title='Ingredient',),
    title= '20 Most Common Ingredients', titlefont = dict(size = 20),
    margin=dict(l=150,r=10,b=60,t=60,pad=5),
    width=800, height=500, 
)
data = [trace]
fig = go.Figure(data=data, layout=layout)
plot(fig, filename='horizontal-bar')



