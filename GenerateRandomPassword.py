# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:06:06 2023

@author: KIIT
"""

import random as r
import string as s
print(s.ascii_letters)
passw=r.sample(s.ascii_letters, 7)
passw="".join(passw)
print("The generate random password is :",passw)