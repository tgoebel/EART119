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
#------------my modules-----------------------
import data.seis_utils as seis_utils
import Optimize.opt_utils as opt_utils
#--------------------------0---------------------------------------------
#                     params, dirs, files
#------------------------------------------------------------------------
data_dir = '%s/PycharmProjects/EART119/data'%( os.path.expanduser( '~'))
file_in  = 'prague_aftershock.txt'
file_clean = file_in.replace( '.txt', '_clean.txt')
dPar  =  { 'k'    : 5,
           'MSmag': 5.7, #for a specific MS event having the event ID would be better, but MAG works here
           # event selection
           'rmax' : 10**(0.25*5.7-.22), #16, # for power-law fitting
           # time range for PL fit
           'tmin'  : 1, 'tmax' : 100,
           'testPlot' : True,
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

#--------------------------2---------------------------------------------
#                  initial processing steps
#------------------------------------------------------------------------
#A# select events within certain radius from MS
MS_ID = np.arange( mData[0].shape[0])[mData[9] == dPar['MSmag']]
aR    = seis_utils.haversine( mData[7][MS_ID], mData[6][MS_ID], mData[7], mData[6])
selR  = aR <= dPar['rmax']
print 'maximum radius', dPar['rmax'], 'N filtered events: ', selR.shape[0]-selR.sum()
mData = mData.T[selR].T
print 'events within rmax', selR.sum()
# plt.figure()
# plt.plot( mData[7], mData[6], 'ko')
# plt.show()

#B# select M5.7 mainshock for smaller data-set
MS_ID = np.arange( mData[0].shape[0])[mData[9] == dPar['MSmag']]

#C# create time vector ignoring leap years etc.
at_days = mData[0]*365 + mData[1]*365/12 + mData[2]  + mData[3]/24 + mData[4]/(24*60) + mData[5]/(24*3600)



#D# determine temporal decay rates
at_bin, aN_bin = seis_utils.eqRate( at_days, dPar['k'])
at_bin_tmp, aN_bin_tmp   = seis_utils.eqRate( at_days[MS_ID::], dPar['k'])
if dPar['testPlot'] == True:
    plt.figure()
    ax = plt.subplot( 111)
    ax.semilogy( at_bin/365, aN_bin, 'ko', label = 'all events')


    ax.semilogy( at_bin_tmp/365, aN_bin_tmp , 'ro', mec= 'r', mew = 1.5, label = 'Aftershocks')
    ax.legend( loc = 'upper left')
    ax.set_xlabel( 'Time [dec. year]')
    ax.set_ylabel( 'events/day')
    plt.show()

#--------------------------3---------------------------------------------
#                    power-law fitting
#------------------------------------------------------------------------
# subtract t MS from aftershock times - new vector has only AS with time relative to MS in days
at_AS = at_days[MS_ID+1::] - at_days[MS_ID]
# compute rates
at_bin_AS, aN_bin_AS   = seis_utils.eqRate( at_AS, dPar['k'])
# power law fit
sel_t = np.logical_and( at_bin_AS >= dPar['tmin'], at_bin_AS <= dPar['tmax'])

dPL = opt_utils.lin_LS( np.log10( at_bin_AS[sel_t]), np.log10( aN_bin_AS[sel_t]))
p_omori = dPL['b']
print 'Omori p-value: ', p_omori
# for dN/dt = c*t**(-p);
aOmori_rate = 10**( np.log10( at_bin_AS)*p_omori + dPL['a'])

#--------------------------4---------------------------------------------
#                    plots
#------------------------------------------------------------------------
plt.figure()
ax = plt.subplot()
ax.loglog( at_bin_AS, aN_bin_AS, 'ko', mfc = 'none', mew = 1.5, label = 'aftershocks, $N_{tot}$=%i'%( at_AS.shape[0]))
ax.loglog( at_bin_AS, aOmori_rate, 'r--', label = 'Omori, $p$=%.2f'%( p_omori))

ax.legend( loc = 'upper right')
ax.set_xlabel( 'Time [day]')
ax.set_ylabel( 'events/day')
plt.savefig( file_in.replace( '.txt', 'Omori.png'))
plt.show()











