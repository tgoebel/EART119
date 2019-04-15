# -*- coding: utf-8 -*-
# python 2.7
'''
Created on April 13, 2019

    -  plotting examples

@author: tgoebel
'''
import numpy as np
import matplotlib.pyplot as plt
#=========================================================
#                   variables
#=========================================================
N  = 100
aX = np.linspace( 0, 2*np.pi, N)
aSin = np.sin( aX)
aCos = np.cos( aX)

def cos_sin( x):
    """
    create a matrix where every column, i  =  sin(x_i) + cos(x)
    so that cos + sin varies between +/- 2
    :param x:
    :param y:
    :return:
    """
    #print np.array([1,2]) + np.array([[3],[4]])
    return np.cos( x) + np.sin( x).reshape( -1, 1)

#=========================================================
#               scatter and line plots
#=========================================================
plt.figure(1, figsize = (12, 6))
ax1 = plt.subplot(311)
ax1.plot( aX, aSin, 'ko')
ax1.set_ylabel( 'sin(x)')
ax2 = plt.subplot(312)
ax2.plot( aX, aSin, 'k-')
ax2.plot( aX, np.cos(aX), 'k-')
ax2.plot( aX, np.cos(aX)+aSin, 'r-')
ax3 = plt.subplot(313)
ax3.scatter( aX, aSin, c = aSin)
ax3.set_xlabel( ' x')

#=========================================================
#              colormaps contors etc
#=========================================================
plt.figure(2)
ax2 = plt.subplot( 111)
ax2.imshow( cos_sin(aX))

plt.figure(3)
ax2 = plt.subplot( 111)
print cos_sin(aX).min(), cos_sin(aX).max()
plot2 = ax2.imshow( cos_sin(aX), extent = (0, 2*np.pi, 0, 2*np.pi))
plt.colorbar( plot2)
plt.show()
