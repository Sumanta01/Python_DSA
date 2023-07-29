# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:32:25 2023

@author: KIIT
"""
import random
import numpy as np
import matplotlib.pyplot as plt

def GenerateNumber(n):
    val=[]
    for i in range(n):
        e_val=np.random.randn()
        val.append(e_val)
        
    return val

data=GenerateNumber(100)
plt.plot(data,color='red')
#plt.hist(data,color='red')
plt.show()

        
    