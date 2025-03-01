# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:58:18 2023

@author: KIIT
"""

from queue import Queue
q=Queue(maxsize=3)
q.put(22)
q.put(12)
q.put(43)

print(q.get())
print(q.get())

print(q.qsize())