# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 23:22:02 2023

@author: KIIT
"""

import cv2
img=cv2.imread('Mac.jpg')
img_resize=cv2.resize(img, (987,700))

if img_resize is None:
    print("Unable to read image")
    exit(0)
    
cv2.imshow('Image', img_resize)
cv2.waitKey(0)