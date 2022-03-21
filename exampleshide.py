# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 01:54:27 2022

@author: Carlos Costa
"""

#import hidetext as h
from spymod import Spy
import cv2

t=Spy()

origin="iseg.png"
destination="iseg2022.png"

hiddenimage=t.hide(origin,"hidden text.")
cv2.imwrite(destination, hiddenimage)
