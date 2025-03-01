# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:51:03 2023

@author: KIIT
"""

from collections import deque
q=deque()
print(type(q))

#INSERT
q.appendleft(11)
q.appendleft(43)
q.appendleft(21)
q.appendleft(87)

print(q)
print(q.pop())
print(q.popleft())