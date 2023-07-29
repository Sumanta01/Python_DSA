# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 02:16:33 2023

@author: KIIT
"""

class AgeError(Exception):
    pass



try :
    age=int(input("Enter your age :"))
    
    if(age<=18):
        raise AgeError
        
    else:
        print(" Congratulations You are eligible for voting...")
        

except Exception as e:
    print("Unfortunately You are not eligible for voting...")
    
finally: #Execute everytime
    print("Wheather the exception handle or not finally block execute first ")