# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 00:15:07 2023

@author: KIIT
"""

import threading

def hello(name):
    print("Hii",name)
    

def bye(name):
    print("Byee",name)
    
    
if __name__=='__main__':
    
    t1=threading.Thread(target=hello,args=("Sumanta",))
    t2=threading.Thread(target=bye,args=("Sumanta",))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Done !")