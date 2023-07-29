# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 01:16:50 2023

@author: KIIT
"""
import threading
x=0
def increment():
    global x
    x+=1

def thread_task(lock):
    for i in range (100000):
        lock.acquire()
        increment()
        lock.release()
        
        
def fun ():
    global x
    x=0
    lock=threading.Lock()
    
    t1=threading.Thread(target=thread_task,args=(lock,))
    t2=threading.Thread(target=thread_task,args=(lock,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    

if __name__=='__main__':
    for i in range(15):
        fun()
        print(f"Iteration: {i} ,X: {x}")

