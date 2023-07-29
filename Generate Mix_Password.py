# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:17:28 2023

@author: KIIT
"""

import random as r
import string as s
print(s.ascii_letters+s.digits)
mixPas=r.sample(s.ascii_letters + s.digits, 9)
print(mixPas)
mixPas="".join(mixPas)
print("The Generate mix Pasword is :",mixPas)