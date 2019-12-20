# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:10:11 2019

@author: CEC
"""

##    Manejo de archivos

import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([(1,2,3),(4,5,6)])
print(b)


array=np.array([(1,2,3,4),(5,6,7,8)], dtype=np.int64)
print(array)

unos=np.ones((3,4))
print(unos)

ceros=np.zeros((3,4))
print(ceros)

## Matriz con valores espaciados

espacio1=np.arange(0,30,5)
print(espacio1)

espacio2=np.linspace(0,2,5)
print(espacio2)

##  Matriz identidad
identidad=np.eye(4,4)
print(identidad)

identidad2=np.identity(4)
print(identidad2)

##   Conocer dimensiones de una matriz
c=np.array([(1,2,3),(4,5,6)])
print(c.ndim)

##   Conocer el tipo
d=np.array([(1,2,3)])
print(d.dtype)

##   Conocer el tamaño y forma de matriz
e=np.array([(1,2,3,4,5,6)])
print(e.size)
print(e.shape)

##   Cambio de forma de matriz
f=np.array([(8,9,10),(11,12,13)])
print(f)
print("\n"*2)
f=f.reshape(3,2)
print(f)

##   Para mostrar un valor de la matriz
g=np.array([(1,2,3,4),
            (3,4,5,6)])
print(g)
print("\n"*1)
print(g[1,3])

##   Para mostrar la fila
g=np.array([(1,2,3,4),
            (3,4,5,6)])
print(g[0:,1])

##   Para sacar min, max y sumar la matriz
h=np.array([2,4,8])
print(h.min())
print(h.max())
print(h.sum())

##   Raiz cuadrada
i=np.array([(1,2,3),(3,4,5)])
print("\n"*2)
print(np.sqrt(i))
print("\n"*2)
print(np.std(i))

## Suma,resta, Multiplicacion y Division
j=np.array([(1,2,3),
            (3,4,5)])
k=np.array([(1,2,3),
            (3,4,5)])
print(j+k)
print("\n")
print(j-k)
print("\n")
print(j*k)
print("\n")
print(j/k)

##   Producto punto
l=np.array([[1,2],[3,4]])
m=np.array([[11,12],[13,14]])
print(np.dot(l,m)) 

##  Pandas
import pandas as pd
data=np.array([["","col1","col2"],["Fila1",11,22],["Fila2",33,44]])
print(pd.DataFrame(data=data[1:,1:],index=data[1:,0],columns=data[0,1:]))
