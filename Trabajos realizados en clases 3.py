# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:14:32 2019

@author: CEC
"""

#TRABAJOS VISTO EN CLASE 3

a=1
b=100
if a==b:
    print("El valor si es igual")
else:
    print("El valor no es igual")

aclnum=int(input("What is the IPv4 ACL number? "))
if aclnum>=1 and aclnum<=99:
    print("This is a standard IPv4 ACL.")
elif aclnum>=100 and aclnum<=199:
    print("This is a extendfed IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")


   
#Bucle for loop
    
    
devices=["R1","R2","R3","S1","S2"]
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)

#Bucle while

x=input("ingrese el numero: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break
  

while True:
    x=input("Ingrese el numero a contar: ")
    if x=="q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
 


for i in range(3):
    print(i)


 
result=0
n=5
for a in range(1, n+1):
    result +=1
    #lo de arriba es igual a: result=result+1
    print(result)

for i in range(10,0,-2):
    print(i)



#FUNCIONES

def hi(name):
    print("Hi,", name)
hi("greg")

def hiall(na1,na2):
    print("Hi,",na1)
    print("Hi,",na2)
hiall("Kevin","Andres")

def address(street,city,postalcode):
    print("Your address is: ")
    
s=input("street: ")
pc=input("postalcode: ")
c=input("city: ")
address=(s,c,pc)



def subtra1(a,b):
    print(a-b)

subtra1(5,2)
subtra1(2,5)

def subtra2(a,b):
    print(a-b)
subtra2(a=5,b=2)
subtra2(b=2,a=5)

def subtra3(a,b):
    print(a-b)
subtra3(5,b=2)
subtra3(5,2)


def multifly(a,b):
    return a*b
print(multifly(3,4))

def wishes():
    print("My wishes")
    return "Happy birthday!"
    
print(wishes())

def hola(lista):
    for name in lista:
        print("Hi,",name)
hola(["Kevin","Andres","Pedro"])

def createlist(n):
    mylist=[]
    for i in range(n):
        mylist.append(i)
    return mylist
print(createlist(5))














































