# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 01:03:09 2023

@author: KIIT
"""

import threading
import os

def hello():
    print(f"Nmae: {threading.current_thread().name}")
    print(f"PID: {os.getpid()}")
    
def bye():
    print(f"Name:{threading.current_thread().name}")
    print(f"PID: {os.getpid()}")
    

if __name__=='__main__':
    
    print(f"Process PID: {os.getpid()}")
    print(f"Process Name: {threading.current_thread().name}")
    
    t1=threading.Thread(target=hello,name="T1")
    t2=threading.Thread(target=hello,name="T2")
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Done !...")