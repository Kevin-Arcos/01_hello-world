# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:13:30 2019

@author: CEC
"""

def readInt(prompt, min, max):
    while (True):
        try:
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
            break
        except ValueError:
            print("Wrong input")
        except:
            print("The value is not within permitted range (-10..10)")
    
v = readInt("Enter a number from -10 to 10:", -10, 10)

print("The number is:", v)
