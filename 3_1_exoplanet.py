# -*- coding: utf-8 -*-
# python 2.7
'''
Created on April 13, 2019

    - import ASCII data and determine depth of planet transit in front of a star

    depth = Ap/As = ( Rp/Rs)**2

@author: tgoebel
'''
import numpy as np
import matplotlib.pyplot as plt

#=========================================================
#                   variables, files etc.
#=========================================================
file_in = '../data/exoplanet_transit.csv'

r_earth = 6370    # [km]
r_star  = 800*1e2 # [km]

nPeriod = 3
#=========================================================
#                 load data
#=========================================================
mData = np.loadtxt( file_in, delimiter = ',').T
N     = len( mData[0])
N_P   =  int( float(N)/nPeriod)# length of each transit period

# determine average duration of transit
aDiff = mData[1][1::] - mData[1][0:-1]

# separate the time series in three equal size vectors
aDepth = np.zeros( nPeriod)
for i in range( nPeriod):
    # create index vector
    aID = np.arange( N_P) + N_P*i
    #print aID
    selMin = aDiff[aID] == aDiff[aID].min()
    selMax = aDiff[aID] == aDiff[aID].max()

    ID_min = aID[selMin][0]
    ID_max = aID[selMax][0]
    # determine mean depth of transit (=relative change in star brigthness)
    print 1- mData[1,ID_min:ID_max].mean()
    aDepth[i] = 1 - mData[1,ID_min:ID_max].mean()
    # plt.figure(1)
    # plt.plot( mData[0][aID], mData[1][aID], 'ko')
    # plt.plot( [mData[0,ID_min], mData[0,ID_min]], plt.gca().get_ylim(), 'r--')
    # plt.plot( [mData[0][aID][selMax][0], mData[0][aID][selMax][0]], plt.gca().get_ylim(), 'r--')
    # plt.show()

# compute the size of the planet
aR_p = np.sqrt( aDepth)*r_star
print( 'size of planet', aR_p, 'km')
# compare the size to earth
print( 'size relative to Earth', (aR_p/r_earth))
#=========================================================
#                plot data
#=========================================================
plt.figure(1)
plt.plot( mData[0], mData[1], 'ko')
plt.xlabel('Time [hr]')
plt.ylabel( 'Relative Brightness')

plt.figure(2)
plt.subplot(211)
plt.plot( mData[0],  mData[1], 'ko')
plt.ylabel( 'Relative Brightness')
plt.subplot(212)
plt.plot( mData[0, 0:-1], aDiff*1e2, 'ro')
plt.xlabel('Time [hr]')
plt.ylabel( 'Change in Relative Brightness [%]')
plt.show()
