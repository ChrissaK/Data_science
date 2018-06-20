# -*- coding: utf-8 -*-

import csv

datapath = r'C:\Users\chris\Documents\Data science_Christopher Brooks\course1_downloads\\'
filename = 'mpg.csv'
filenamefull = datapath + filename

with open(filenamefull) as csvfile:
    mpg = list(csv.DictReader(csvfile))


len_dict = len(mpg)

categories = mpg[0].keys()
