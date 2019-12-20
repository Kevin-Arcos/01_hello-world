# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:28:44 2019

@author: CEC
"""


# Primer Forma
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
        
for i in range(1,20):
    if isPrime(i+1):
        print(i+1,end=" ")
print()

# Segunda Forma
def is_Prime(x):
    if x<2:
        return False
    elif x==2:
        return False
    for n in range(2,x):
        if x%n==0:
            return False
    return True
print(is_Prime(5))
for a in range(1,20):
    if is_Prime(a+1):
        print(a+1,end=" ")
print()
    
