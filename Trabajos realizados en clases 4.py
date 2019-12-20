# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:02:09 2019

@author: CEC
"""

import math
x=float(input("Enter x; "))
y= math.sqrt(x)
print("The square root of",x,"equals to",y)




##  Ejemplo de error 
value=1
value/=0

list=[]
x=list[0]



##  Manejo de exepciones
try:
    print("1")
    x=1/0
    print("2")
except:
    print("Oh dear, something went wrong... ")
    
print("3")




##    Tipos de excepciones
try:
    x=int(input("Enter a number: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry")
except ValueError:
    print("You must enter an integer value")
except:
    print("Oh dear, something went wrong...")
print("ThE END!!")




##     Pruena de jerarquia
try:
    y=1/0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Divsion!!")

print("ThE EnD!!")



##   Ejemplos de exepciones con variables
def badFun(n):
    try:
        return 1/n
    except ArithmeticError:
        print("Arithmetic problem!!")
    return None
badFun(0)
print("The End!!")


def bad(k):
    return 1/k
try:
    bad(0)
except ArithmeticError:
    print("What happenig?? An exception was raised")
print("ThE EnD!!")
    

