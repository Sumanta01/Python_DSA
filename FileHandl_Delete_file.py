# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 03:04:56 2023

@author: KIIT
"""

import os

if os.path.exists("NLP_Copy.txt"):
    os.remove("NLP_Copy.txt")
    
else:
    print("The file does not exist")
