# -*- coding: utf-8 -*-
"""
Created on Mon May 22 18:52:43 2023

@author: KIIT
"""
#Keys

my_dict={234:"cat",64:"beer",43:"dog",123:"rat",22:"deer"}

d=sorted(my_dict.keys())
dict_1={}
for i in d:
     
     dict_1[i]=my_dict[i]
     
     
print(dict_1)


# Values

my_dic={234:"cat",64:"beer",43:"dog",123:"rat",22:"deer"}

dic_2= { key:value for key , value in sorted(my_dic.items(),key=lambda c:c[1])}

print(dic_2)