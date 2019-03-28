'''
Created on Jan 23, 2016

- plot seismicity rates, magnitudes and injection rates at KTB site


@author: tgoebel
'''

import os
import numpy as np
import pylab as plb

#===================================================================================
#                         dir, file, and parameter
#===================================================================================
# for seism rate
win,step = 40, 10
binsize  = 10 # in hr
#  variables
t0 = float( ) # starting time of time axis
aT     = np.array([]) # time of seismicity
aMag   = np.array([]) # magnitudes
aT_inj = np.array([]) # time of injections
aV     = np.array([]) # injected volume
aBin,aRate = np.array([]), np.array([]) # bins and seismicity rates

catName   = 'KTB'
dataDir   = '%s/Documents/teaching/python_obspy/data'%( os.path.expanduser( '~'))

magFile   = '%s_mag.txt'%(    catName)
injFile   = '%s_inject.txt'%( catName)

plotFile  = 'KTB_rate.png'

#===========================1========================================================
#                       load data
#====================================================================================
os.chdir( dataDir)
#magnitudes
mData = np.loadtxt( magFile, comments = '#').T
aT,aMag = mData[0], mData[1]

# injection rate
mData = np.loadtxt( injFile, comments = '#').T
aT_inj, aV  = mData[3], mData[4]



# substract initial time in sec and convert to hr
if aT_inj[0] < aT[0]:
    t0 = aT_inj[0]
else: 
    t0 = aT[0]
aT_inj, aT = (aT_inj - t0)/3600, (aT - t0)/3600
# define new t0 in new time coordiante system in hr 
t0 = np.array([aT_inj[0], aT[0]]).min()
#===========================2========================================================
#                       get average injection rate
#====================================================================================
# get average injection rate
sel = aV > 0
aT_inj, aV = aT_inj[sel], aV[sel]
import scipy.stats 
#stderr is standard error of y
slope, intercept, R, prob, stderr = scipy.stats.linregress( aT_inj, aV )
print 'ave. inject rate: %.2f m3/hr'%(slope), R, prob, stderr 

#===========================3========================================================
#                      compute seismicity rates
#====================================================================================
# smoothed rate from overlapping sample windows normalized by delta_t
aS = np.arange( 0, aT.shape[0]-win, step)
aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
iS = 0
for s in aS:
    i1, i2 = s, s+win
    aBin[iS]  = 0.5*( aT[i1]+aT[i2])
    aRate[iS] = win/( aT[i2]-aT[i1]) 
    iS += 1

# alternatively just use histogram
aHist_bins = np.arange( aT[0], aT[-1]+binsize, binsize)
aN, aHist_bins = np.histogram( aT, aHist_bins)
# correct for binsize
aN /= binsize

# make sure bins and histogram have same length
mRate = np.array(zip(*zip(aN, aHist_bins)))  
aN, aHist_bins = mRate[0], mRate[1]
#===========================4========================================================
#                      plotting
#====================================================================================
plb.figure(1)
ax1 = plb.subplot( 311)
ax1.plot( aT, aMag, 'ko')
ax1.set_xlabel( 'Time [hr]'), ax1.set_ylabel( 'Mag')
ax1.set_xlim( t0, ax1.get_xlim()[1])

ax2 = plb.subplot( 312)
ax2.plot( aT_inj, aV*1e-4, 'b-', lw =1.5, label = 'ave. inject rate: %.2f m3/hr'%(slope))
ax2.set_xlabel( 'Time [hr]'), ax2.set_ylabel( 'Cum. Inject. [1e4 m3]')
ax2.legend( loc = 'upper left')

ax3 = plb.subplot( 313)
ax3.plot( aHist_bins, aN, 'g-')
ax3.plot( aBin, aRate, 'r-', lw = 1.5)
ax3.set_xlabel( 'Time [hr]')
ax3.set_ylabel( 'No. events per hour')


#===========================5========================================================
#                      save figure
#====================================================================================
os.chdir( dataDir)
plb.savefig( plotFile, dpi = 200)
plb.show()












