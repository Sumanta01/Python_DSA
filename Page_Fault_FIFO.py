# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 21:26:11 2023

@author: KIIT
"""

def FIFO_Page_Fault(string_ref,no_frames):
    page_fault=0
    frames=[]
    for i in string_ref:
        if i not in frames:
            page_fault+=1
            frames.append(i)
            
        if len(frames)>no_frames:
            frames.pop(0)
            
    return page_fault
            
        
        

if __name__=="__main__"    :
   ref_str=[4, 7, 6, 1, 7, 6, 1, 2, 7, 2]
   no_frames=3
   res=FIFO_Page_Fault(ref_str, no_frames)
   print(res)