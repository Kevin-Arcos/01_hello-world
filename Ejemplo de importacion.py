# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:46:34 2019

@author: CEC
"""
import datetime
oTime=datetime.datetime.now()
print(oTime.isoformat())

from platform import platform

print(platform())
print(platform(1))
print(platform(0,1))

import numpy as np


from platform import machine
print(machine())


import math as m
print(m.sin(m.pi/2))

from math import e, exp, log
print(pow(e,1)==exp(log(e)))
print(pow(2,2)==exp(2*log(2)))
print(pow(e,3)==exp(0))

