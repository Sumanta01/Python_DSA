# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:58:01 2023

@author: KIIT
"""

def add_decorator(add_func):
    
    def wrapper(a, b):
        print("Adding two numbers...")
        result = add_func(a, b)
        print("The result is:", result)
        return result
    return wrapper


@add_decorator
def add_numbers(a, b):
    return a + b

# Usage
result = add_numbers(54, 5)

    