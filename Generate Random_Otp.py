# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:14:08 2023

@author: KIIT
"""

import random as r
import string as s
#print(s.digits)
otp=r.sample(s.digits, 6)
otp="".join(otp)
print("The Generate random otp is:",otp)