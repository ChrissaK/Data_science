# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 13:33:51 2018

@author: chris
"""

import pandas as pd
import os

def answer_five():
    mask=(census_df['SUMLEV']==50) # real counties are marked with SUMLEV=50
    census_df1 = census_df[mask]
    census_df2 = census_df1.groupby('STNAME')
    return census_df2.size().idxmax()

def answer_six():
    mask=(census_df['SUMLEV']==50) # real counties are marked with SUMLEV=50
    census_df1 = census_df[mask]
    states_population = {}
    for state in set(census_df['STNAME']):
        cities_df = census_df1[census_df1['STNAME']==state].sort_values('CENSUS2010POP',ascending=False)[0:3]
        states_population[state] = cities_df['CENSUS2010POP'].sum()
    
    sorted_states = sorted(states_population.items(), key=lambda x:x[1], reverse=True)
    answer = []
    for state in sorted_states: 
        answer.append(state[0])
    return answer[0:3]

def answer_seven():
    mask=(census_df['SUMLEV']==50) # real counties are marked with SUMLEV=50
    census_df1 = census_df[mask]
    pop_strings = ['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013',
                'POPESTIMATE2014','POPESTIMATE2015']
    county_popdiff = []
    for ind in census_df1.index:
        county_pop = []
        for k in range(len(pop_strings)):
            county_pop.append(census_df1.loc[ind][pop_strings[k]])  #create a list with population numbers for the county
            list_temp = []  # contains the population differences over the period of 5 years
            for k in range(len(pop_strings)):
                [list_temp.append(abs(j-i)) for i, j in zip(county_pop[k:-1], county_pop[k+1:])]
        county_popdiff.append(list_temp)
        
    max_popdiff = [max(sublist) for sublist in county_popdiff]   
    county_ind = max_popdiff.index(max(max_popdiff))
    answer = census_df1.loc[census_df1.index[county_ind]]['CTYNAME']
    
    return answer


def answer_eight():
    isreg1 = (census_df['REGION']==1)
    isreg2 = (census_df['REGION']==2)
    istruecounty = (census_df['SUMLEV']==50)
    isgreaterpop = (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014'])
    counties = census_df['CTYNAME'].values
    iswashington = [True if item.split(' ')[0]=='Washington' else False for item in counties]
    
    df1 = census_df[(isreg1 | isreg2) & istruecounty & isgreaterpop & iswashington]
    df1_new = df1[['STNAME', 'CTYNAME']].copy()
    

    return df1_new
        
    
        
    
    
    
headPATH, tailPATH = os.path.split(os.getcwd())
dataPATH = os.path.join(headPATH,'course1_downloads')
filename = os.path.join(dataPATH,'census.csv')


census_df = pd.read_csv(filename)


# Q5: Which state has the most counties in it? (hint: consider the sumlevel 
#     key carefully! You'll need this for future questions too...)
#     This function should return a single string value.
print(answer_five())

# Q6: Only looking at the three most populous counties for each state, 
#     what are the three most populous states (in order of highest population 
#     to lowest population)? Use CENSUS2010POP.
#     This function should return a list of string values.
print(answer_six())

# Q7: Which county has had the largest absolute change in population within 
#     the period 2010-2015? (Hint: population values are stored in columns 
#     POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
#     e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 
#     130, then its largest change in the period would be |130-80| = 50.
#     This function should return a single string value.
print(answer_seven())

# Q8: In this datafile, the United States is broken up into four regions using 
#     the "REGION" column.
#     Create a query that finds the counties that belong to regions 1 or 2, 
#     whose name starts with 'Washington', and whose POPESTIMATE2015 was greater 
#     than their POPESTIMATE 2014.
#     This function should return a 5x2 DataFrame with the columns = ['STNAME',
#    'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).
print(answer_eight())