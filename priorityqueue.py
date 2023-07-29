# -*- coding: utf-8 -*-
"""
Created on Thu May 11 02:07:09 2023

@author: KIIT
"""

import queue
q=queue.PriorityQueue()
q.put(22)
q.put(12)
q.put(72)
q.put(2)
q.put(32)
q.put(92)
q.put(7)

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())