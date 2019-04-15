#!/bin/python2.7
"""

--> 1) load ANSS seismicity data and well locations for Oklahoma
--> 2) plots eq rates
--> 3) plot rates for
--> 4) compute aftershock decay rates and power-law fit



"""
from __future__ import division
import os
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.basemap import Basemap as Basemap




#------------my modules-----------------------
import data.seis_utils as seis_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir   = '%s/PycharmProjects/EART119/data'%( os.path.expanduser( '~'))
file_eq    = 'seism_OK.txt'
file_well  = 'injWell_OK.txt'


dPar  =  {   'nClicks' : 10,
             'tmin'    : 2010,
             # -----basemap params----------------------
             'xmin' : -101, 'xmax' : -94,
             'ymin' :   33.5, 'ymax' :  37.1,
             'projection' : 'aea',# or 'cea' 'aea' for equal area projections
           }

#--------------------------1---------------------------------------------
#                        load data
#------------------------------------------------------------------------
os.chdir( data_dir)
# load seismicity and well data using loadtxt
mSeis  = np.loadtxt( file_eq).T
aTime  = seis_utils.dateTime2decYr( mSeis[1], mSeis[2], mSeis[3], mSeis[4], mSeis[5],mSeis[6])
mSeis  = np.array( [aTime, mSeis[7], mSeis[8], mSeis[-1]])
# select most recent seismic events
sel    = mSeis[0] >= dPar['tmin']
mSeis  = mSeis.T[sel].T
mWells = np.loadtxt( file_well).T



#--------------------------2---------------------------------------------
#                       map view, select boundaries of seismicity
#------------------------------------------------------------------------
plt.figure(1)
ax1 = plt.subplot(111)
ax1.plot( mWells[2], mWells[3], 'bv', ms = 2, mew = 1.5, mfc = 'none', alpha = .5)
ax1.plot( mSeis[1], mSeis[2],   'ro', ms = 5, mew = 1.5, mfc = 'none')
print("Please click %i times"%( dPar['nClicks']))
tCoord = plt.ginput( dPar['nClicks'])
print("clicked", tCoord)
plt.show()

aLon =  np.array( tCoord).T[0]
aLat =  np.array( tCoord).T[1]


# project into equal area coordinate system
lon_0, lat_0 = .5*( dPar['xmin']+dPar['xmax']), .5*( dPar['ymin']+dPar['ymax'])
m = Basemap(llcrnrlon = dPar['xmin'], urcrnrlon=dPar['xmax'],
            llcrnrlat = dPar['ymin'], urcrnrlat=dPar['ymax'],
            projection=dPar['projection'], lon_0 = lon_0, lat_0 = lat_0)

aX, aY = m(  aLon, aLat)
#print aX*1e-3
#print aY*1e-3

#--------------------------3---------------------------------------------
#               compute affected area
#------------------------------------------------------------------------
A_seis = seis_utils.area_poly_vec( aX*1e-3, aY*1e-3)
print 'total area affected by seismicity: ', A_seis
print 'fraction of area of OK', A_seis/(181*1e3) # about 1/3







