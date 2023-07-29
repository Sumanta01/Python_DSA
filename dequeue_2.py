# -*- coding: utf-8 -*-
"""
Created on Sat May  6 00:55:56 2023

@author: KIIT
"""

import collections
q=collections.deque()
q.appendleft(33)
q.appendleft(65)
q.appendleft(43)
print(q)
q.pop()
print(q)


import queue
Q=queue.Queue()
Q.put(3)
Q.put(87)
Q.put(54)
print(Q)
print(Q.get())
print(Q.get())
print(Q.get())

