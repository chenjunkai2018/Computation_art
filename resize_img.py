# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:00:31 2021

@author: shini
"""

import os

import cv2

img_path = './data/input2.png'

img = cv2.imread(img_path)

img_out = cv2.resize(img, (200, 200))

cv2.imwrite('input2_s.png', img_out)