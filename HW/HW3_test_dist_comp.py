#!/bin/python2.7
"""

--> 1) load ANSS (or comcat) seismicity data using np.genfromtxt
--> 2) create time vector in days
--> 3) select events within area of interest
--> 4) compute aftershock decay rates and power-law fit



"""
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from mpl_toolkits.basemap import Basemap
#------------my modules-----------------------
import data.seis_utils as seis_utils
import Optimize.opt_utils as opt_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = '%s/PycharmProjects/EART119/data'%( os.path.expanduser( '~'))
file_in    = 'prague_aftershock_clean.txt'
file_clean = file_in.replace( '.txt', '_clean.txt')
dPar  =  { 'k'    : 5,
           'MSmag': 5.7, #for a specific MS event having the event ID would be better, but MAG works here
           # event selection
           'rmax' : 10**(0.25*5.7-.22), #16, # for power-law fitting
           # time range for PL fit
           'tmin'  : 1, 'tmax' : 100,
           'testPlot' : False,
           }

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
os.chdir( data_dir)
# remove special characters from date time for simpler data import
if os.path.isfile( file_clean):
    print '%s exists'%( file_clean)
else:
    os.system( "sed -e 's/[:\/]/ /g' %s > %s"%( file_in, file_clean))
# import cleaned file, first 10 columns, 6 time columns, 3 loc, 1 MAG
#                                             date  time la  lo, dep, mag
mData   = np.genfromtxt( file_clean, usecols=(0,1,2,3,4,5,6, 7,  8,   9), skip_header = 2).T
print( 'total no. of eqs.', mData[0].shape[0])

#--------------------------2---------------------------------------------
#                  initial processing steps
#------------------------------------------------------------------------
#A# select events within certain radius from MS
MS_ID = np.arange( mData[0].shape[0])[mData[9] == dPar['MSmag']]
print( mData[7][MS_ID], mData[6][MS_ID])
aR    = seis_utils.haversine( mData[7][MS_ID], mData[6][MS_ID], mData[7], mData[6])

def mapDist( lon1, lat1, lon2, lat2):
    minLat = np.hstack( (lat1, lat2)).min()#longitudes and latitudes from data
    maxLat = np.hstack( (lat1, lat2)).max()
    minLon = np.hstack( (lon1, lon2)).min()
    maxLon = np.hstack( (lon1, lon2)).max()
    lon_0, lat_0 = .5*(minLon+maxLon), .5*(minLat+maxLat)
    m = Basemap(    projection = 'aeqd',
                    llcrnrlon = minLon, urcrnrlon=maxLon,
                    llcrnrlat = minLat, urcrnrlat=maxLat,
                    lon_0 = lon_0, lat_0 = lat_0)

    x_1, y_1 = m( lon1, lat1)
    x_2, y_2 = m( lon2, lat2)
    dist = np.sqrt((x_1-x_2)**2+(y_1-y_2)**2)
    return dist

aR2 = mapDist( mData[7][MS_ID], mData[6][MS_ID], mData[7], mData[6])*1e-3
print( aR2[aR2 < dPar['rmax']].shape[0])
print( aR[aR < dPar['rmax']].shape[0])

plt.figure()
plt.subplot(211)
plt.plot( aR, aR2, 'ko')
plt.plot( plt.gca().get_xlim(), plt.gca().get_xlim())
plt.subplot( 212)
plt.plot(  aR, abs(aR-aR2), 'ko')

plt.show()






