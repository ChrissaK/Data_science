# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:22:42 2018

@author: chris
"""
#import string as str

#people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']
#
#def split_title_and_name(person):
#    elements = person.split(' ')
#    title = elements[0]
#    last_name = elements[2]
#    return title, last_name 
#
#faculty_members = list(map(split_title_and_name,people))



# Try with lambdas
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda person:person.split()[0] + 
                               ' ' + person.split()[-1]))
    
    
    
# Create all possible combinations of user ids
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits]