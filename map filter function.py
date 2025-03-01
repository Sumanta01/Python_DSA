# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:52:58 2023

@author: KIIT
"""

lst=["a","abc","bcde","g","fd","o"]
lst.sort(key=lambda x:len(x))
print(lst)
#filter function
l_st=[1,2,3,4,5,6,7,8,9,10]
n_lst=(list(filter(lambda x:(x%2==0),l_st)))
print(n_lst)

#map function
ok_lst=[1,2,3,4,5,6,7,8,9,10]
an_lst=list(map(lambda x:x**3,ok_lst))
print(an_lst)