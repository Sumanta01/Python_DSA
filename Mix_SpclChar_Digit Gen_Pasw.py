# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:28:40 2023

@author: KIIT
"""

import random as r
import string as s

spclchar="~!@#%$^&*()+=}]{[?|_"
print(s.ascii_letters + s.digits + spclchar)

strongPas=r.sample(s.ascii_letters + s.digits + spclchar, 11)
strongPas="".join(strongPas)
print("The Generate mix special character strong Password is : ",strongPas)