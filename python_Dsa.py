# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:17:49 2023

@author: KIIT
"""
#List
lst1=[]
def square(lst):
    for i in lst:
        lst1.append(i*i)
    return lst1

print(square([11,23,5,67,32,35]))

lst=[11,23,5,67,32,35]
print(lst.count(5))
print(lst.pop())
print(lst) 

#Sets
set_1={'apple',12,True,'jack',65,32}
print(set_1)
set_1.add(76)
print(set_1)
set_1.pop()
print(set_1)
set_3=set_1.union({6,'rew',87})
print(set_3)
print(list(set_3))
#Dictionary
my_dict={11:'Cognizant',22:'Capgemini',33:'Tcs',44:'Accenture',55:[1,2,3,4]}
print(my_dict)
print(my_dict[33])
print(my_dict.pop(55))
print(my_dict)
#copy in dictionary
dt={22:'kiit',43:'kims',54:'kiss'}
st=dt.copy()
print(st)
print(dt)
#Tuples
my_tuple=()
print(type(my_tuple))

my_tuple=('Rat',66,'Cat',43,65,43)
print(my_tuple)
print(my_tuple.count(43))
#Tuple can create without parnthesis is called Tuple Packing
my_tuple2=87,76,'sukon',65
print(my_tuple2)
#my_tuple[3]=655#Tuple is immutable
print(my_tuple)
#Lambda Function
addition=lambda a,b:a+b
print(addition(55, 99))


def addition(a ,b):
    return a+b;
print(addition(34, 66))


def natural(n):
    return n*(n+1)/2
print(natural(25))

natural=lambda n:n*(n+1)/2
print(natural(25))

















