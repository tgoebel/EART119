# -*- coding: utf-8 -*-
# python 2.7
'''
Created on April 13, 2019

    - some data handling examples

@author: tgoebel
'''
import numpy as np
import matplotlib.pyplot as plt
import os
#=========================================================
#                   dirs and params
#=========================================================
s_cwd = '../data'
os.chdir( s_cwd)
file_out = 'test1.txt'
#=========================================================
#                   create data
#=========================================================
N  = 10
aX = np.arange( 10)
aY = aX**2

#=========================================================
#               data I/O
#=========================================================
# ASCII
np.savetxt( file_out, np.array( [aX,aY]).T, fmt = ('%4.0f%4.0f'),
            header = 'X   X^2')

print( '--------------numpy-------------')
mData = np.loadtxt( file_out).T
print mData
aX_load = np.genfromtxt( file_out, usecols=(0))
print aX_load

print( '-------------read line by line---------------')
# line-by-line
with open( file_out, 'r') as file_obj:# automatically close file after read
    file_obj.next()# skip header
    for line  in file_obj:
        lStr =  line.split()
        print( float(lStr[0]), int( float(lStr[1])))

print( '-------------binary---------------')
import scipy.io
scipy.io.savemat( file_out.replace( 'txt', 'mat'), { 'X' : mData[0], 'Y' : mData[1]})

dData = scipy.io.loadmat( file_out.replace( 'txt', 'mat'), { 'X' : mData[0], 'Y' : mData[1]})
print dData



