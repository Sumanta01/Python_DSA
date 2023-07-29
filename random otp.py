# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 02:31:18 2023

@author: KIIT
"""

import random

def generate_otp():
    otp = ""
    for _ in range(6):
        otp += str(random.randint(0, 9))
    return otp

# Generate and print OTP
otp = generate_otp()
print("Generated OTP:", otp)
