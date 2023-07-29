# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 03:59:41 2023

@author: KIIT
"""

import geocoder

def currentLocation():
    g = geocoder.ip('me')
    if g.address:
        return g.address
    else:
        return None


location_name = currentLocation()

if location_name:
    print(f"Current Location: {location_name}")
else:
    print("Unable to find the current location.")


#Output:Current Location: Bhubaneshwar, Odisha, IN