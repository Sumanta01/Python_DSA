# -*- coding: utf-8 -*-
"""
Created on Tue May  2 01:30:26 2023

@author: KIIT
"""
import queue
import collections
stack=collections.deque()
print(stack)
stack.append(77)
stack.append(66)
stack.append(12)
stack.append(22)
stack.append(99)
print(stack)
stack.pop()
print(stack)

st=queue.LifoQueue()
print(st)
st.put(22)
st.put(66)
st.put(12)
st.get()
print(st)