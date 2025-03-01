# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:48:53 2023

@author: KIIT
"""

import os

if os.path.exists('Demo.txt'):
    print(os.remove('Demo.txt'))
    
else:
    print("The file didn't exist !!")