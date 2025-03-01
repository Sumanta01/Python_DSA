# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:15:31 2024

@author: KIIT
"""


s = input()

current_word = ""


for char in s:
    
    if char.isupper():
        
        current_word += char.lower()
        
    else:
        current_word += char.upper()


def camelcase_and_print_newline(s):
    words = [s[0]]  
    for char in s[1:]:
        
        if char.islower():
             
            words.append(char)
        else:

            words[-1] += char

    for word in words:
        print(word)
        

camelcase_and_print_newline(current_word)

