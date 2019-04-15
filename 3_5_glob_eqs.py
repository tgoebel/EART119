'''
Created on April 15th, 2019


    - plot an animated map of global earthquake activity


@author: tgoebel
'''
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap

#------------my modules-----------------------
import data.seis_utils as seis_utils

#===================================================================================
#                         files, variables
#===================================================================================
eqFile      = '../data/globalEqs.txt'
xmin, xmax  = -180+1e-4, 180
ymin, ymax  = -90+1e-4, 90

#xmin, xmax  = -180, 0



print xmin, xmax
print ymin, ymax

#===================================================================================
#                         load data
#===================================================================================

aYr  = np.genfromtxt( eqFile, skip_header = 1, usecols=(0), delimiter='-', dtype = int)
mLoc = np.genfromtxt( eqFile, skip_header = 1, usecols=(2,1), delimiter=',', dtype = float).T
# get magnitude information
mLoc = np.genfromtxt( eqFile, skip_header = 1, usecols=(2,1,4), delimiter=',', dtype = float).T
# sort according to year of occurrence
sort_id = aYr.argsort()
aYr = aYr[sort_id]
mLoc= mLoc.T[sort_id].T

#===================================================================================
#                        basemap plotting
#===================================================================================
for it in np.unique( aYr):
    sel_eq = it == aYr
    print( 'current year', it, '#no. of events: ', sel_eq.sum())
    ### create basemap object
    plt.figure( 1)
    plt.cla()
    plt.title( str( it))
    lon_0, lat_0 = .5*( xmin + xmax), .5*( ymin + ymax)
    m = Basemap(projection = 'cyl',
                llcrnrlon = xmin, urcrnrlon=xmax,
                llcrnrlat = ymin, urcrnrlat=ymax,
                 resolution = 'c', lon_0 = lon_0, lat_0 = lat_0)
    m.drawcoastlines()
    aX_eq, aY_eq = m(  mLoc[0][sel_eq], mLoc[1][sel_eq])

    #m.plot(  aX_eq, aY_eq, 'ro', ms = 6, mew = 1.5, mfc = 'none')
    plot1 =     plt.scatter( aX_eq, aY_eq, c = mLoc[2][sel_eq], s = np.exp( mLoc[2][sel_eq]-3))
    cbar  = plt.colorbar( plot1, orientation = 'horizontal')
    cbar.set_label( 'Magnitude')
    #--------------
    #plt.savefig(  file_out, dpi = 150)
    #
    plt.pause( .5)
    #plt.show()
    plt.clf()