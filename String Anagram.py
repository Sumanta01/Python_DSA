# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 01:26:01 2023

@author: KIIT
"""

def checkAnagram(st1 ,st2 ):
    count=0
    if len(st1)!=len(st2):
        print("Not Anagram")
        
    else:
        for i in range (0,len(st1)):
            for j in range(0,len(st2)):
                if st1[i]==st2[j]:
                    count+=1
                    break;
                    
        if count==len(st1):
            print("Anagram")
            
        else:
            print("Not Anagram")
            
            

if __name__=='__main__':
    st1=input()
    st2=input()
    checkAnagram(st1, st2)