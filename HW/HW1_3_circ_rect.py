#!/bin/python2.7
"""
--> maximize side of rectangle b so that area of rectangle is smaller
    than area of circle

"""
import numpy as np

#------------------------------------------------------------------------
#                   params
#------------------------------------------------------------------------
r = 10.6
a = 1.3

#----------------------------1-------------------------------------------
#                   computation
#------------------------------------------------------------------------
b0 = 1
A_circle = np.pi*r**2
A_rect   = a*b0

while A_rect < A_circle:
    b0 += 1
    A_rect = a*b0
    print A_rect, A_circle
b0 -= 1 #take b from the previous step when A_rect < A_circle
print 'largest possible b: ', b0





