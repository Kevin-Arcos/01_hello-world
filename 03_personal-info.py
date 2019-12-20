# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:13:18 2019

@author: CEC
"""


while True:
    a=input("Ingrese su nombre: ")
    b=input("Ingrese su apellido: ")
    c=input("Ingrese su localidad: ")
    space=" "
    x=input("Desea ingresar la edad: ")
    if x=="si":
        d=int(input("Ingrese su edad: "))
        if d>=15 and d<=25:
            print("Es un adolecente")
        elif d>=26 and d<=65:
            print("Es un adulto")
        else:
            print("Es un adulto mayor")
        d=str(d)
        print("Hola"+space+a+space+b+space+"con"+space+d+space+"años bienvenido al"+space+c)
    else:
        if x=="q" or x=="exit":
            break
                   

