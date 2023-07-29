# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 04:07:57 2023

@author: KIIT
"""

import geocoder

def current_location():
    g = geocoder.ip('me')
    if g.latlng:
        latitude, longitude = g.latlng
        return latitude, longitude
    else:
        return None

# Get the current location
location = current_location()

if location:
    latitude, longitude = location
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
else:
    print("Unable to find the current location.")
