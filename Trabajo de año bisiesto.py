# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:41:28 2019

@author: CEC
"""
def isYearLeap(year):
    if(year%4 == 0 and year%100 !=0 or year%400==0):
        return True
    return False

def daysInMonth(year, month):
    if year < 1500 or month <1 or month > 12:
        return None
    meses = [2,4,6,9,11]
    if month not in meses:
        return 31
    elif(isYearLeap(year) and month ==2):
        return 29
    elif month==2:
        return 28
    else:
        return 30

def dayOfYear(year, month, day):
    meses = [2,4,6,9,11]
    if year < 1500 or month <1 or month > 12 or day <1 or day > 31:
        return "Fecha erronea"
    elif not isYearLeap(year) and month == 2 and day > 28:
        return "Fecha erronea"
    elif month in meses and day > 30 :
        return "Fecha erronea"
    days = 0
    for i in range (1,12+1):
        days += daysInMonth(year,i)
    return days

print(dayOfYear(2000, 12, 31))
print(dayOfYear(1989, 2, 29))
print(dayOfYear(1439, 12, 31))
print(dayOfYear(1939, 12, 31))
print(dayOfYear(2019, 11, 31))