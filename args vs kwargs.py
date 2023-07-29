# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:20:37 2023

@author: KIIT
"""

def fun(*args):
    for i in args:
        print(i)

fun(4332,6598,"sexy")





def fun_flex(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)
    
    
fun_flex(vat="MCA",rat="BSc",Sat="MSC")