# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:01:34 2018

@author: chris
"""

import datetime as dt
import time as tm

tm.time() #time returns the current time in seconds since the Epoch. (January 1st, 1970)


#convert timestamp to datetime
dtnow = dt.datetime.fromtimestamp(tm.time())

delta = dt.timedelta(days = 100)  #used for sliding windows
today = dt.date.today()
pday = today - delta