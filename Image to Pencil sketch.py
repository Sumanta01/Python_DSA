# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 03:34:13 2023

@author: KIIT
"""

import cv2

im = cv2.imread("Sumanta.jpeg")


image = cv2.resize(im, (960, 740))
cv2.waitKey(0)

gray_image=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


inverted_image= 255 - gray_image


blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)


outpath = "Pencil Sketch.jpeg"
cv2.imwrite(outpath, pencil_sketch)

cv2.imshow("Original image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)
cv2.waitKey(0)