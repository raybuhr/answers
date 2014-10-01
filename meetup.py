# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 10:26:07 2014

@author: rebuhr
"""

# Calculates the date of meetups. Meetup types are 1st, 2nd, 3rd or 4th week, as well as last or teenth. 

from datetime import date
import calendar

def meetup_day(year, month, day_of_week, meetup_type):
    day = day_of_week.upper()
    c = calendar.monthcalendar(year, month)
    if meetup_type == '1st':
        wk = c[0]
        meetup_date = wk[calendar.day]
    if meetup_type == '2nd':
        wk = c[1]
        meetup_date = wk[calendar.day]
    if meetup_type == '3rd':
        wk = c[2]
        meetup_date = wk[calendar.day]
    if meetup_type == '4th':
        wk = c[3]
        meetup_date = wk[calendar.day]
    if meetup_type == 'last':
        wk = c[-1]
        meetup_date = wk[calendar.day]
    if meetup_type == 'teenth':
        wk = 
        meetup_date = wk[calendar.day]
    return meetup_date