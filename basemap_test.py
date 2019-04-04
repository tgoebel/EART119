'''
Created on Jun 24, 2013

use basemap to plot seismicity
- close up of study region
@author: tgoebel
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import numpy as np

from mpl_toolkits.basemap import Basemap

#===============================================================================
#                 parameters
#===============================================================================
dPar   = { 
           #------------basemap parameters----------------------------------
           
           #set center of map
           'lon_0': -103, 'lat_0' :  38.5,
            #set map boundaries
           'xmin' : -127.5,   'xmax'  :    -81,
           'ymin' :     28,   'ymax'  :     49.5,
           'resolution'         : 'l',
           #---------------------plot parameters--------------------------
           'fontsize'           :  24,
           'textFontsize'       :  24, #in plot texts fontsize
           'plotFormat'         : 'eps', 
           'dpi'                 : 150,
           }

region1 = np.array( [ [ -121, -117, -117, -121, -121], [33.5, 33.5, 36.2, 36.2, 35.5]]) 
region2 = np.array( [ [-103,  -94.2, -94.2, -103,-103], [33.7,33.7,37.05,37.05,33.7]])
#===============================================================================
#                    set up basic map
#===============================================================================
fig = plt.figure(1, figsize=(13.5, 9))
ax  = plt.axes( [.01, .01, .975, .97])

print 'hello'
# setup Lambert Conformal basemap.
m = Basemap( #width=12000000,height=9000000,
             llcrnrlat=dPar['ymin'],urcrnrlat=dPar['ymax'], 
             llcrnrlon=dPar['xmin'],urcrnrlon=dPar['xmax'], 
             projection='merc',lat_0=dPar['lat_0'],lon_0=dPar['lon_0'],
             resolution=dPar['resolution'])


# draw a boundary around the map, fill the background.
# this background will end up being the ocean color, since
# the continents will be drawn on top.
# extra stuff
m.drawmapboundary( fill_color = '#1e90ff') #000080')# 191970')#mid-night  blue#'aqua')

#m.drawrivers(      linewidth=0.5, color='#1e90ff',antialiased=1,ax=None,zorder=5 )
m.drawcoastlines(  linewidth=2.,color='k',antialiased=1,zorder=None )
m.drawcountries(   linewidth=3,color='k',antialiased=1,zorder=None)
m.drawstates(      linewidth=1, color='.5', antialiased=1,  zorder=None )
# fill continents, set lake color same as ocean color.
m.fillcontinents(  color = '.8', lake_color='.5', zorder= 0 )


# draw study regions
vX,vY  = m( region1[0], region1[1])
m.plot( vX,vY, 'r-', lw = 4)
vX,vY  = m( region2[0], region2[1])
m.plot( vX,vY, 'g-', lw = 4)

plt.show()
#===============================================================================
#                  save map
#===============================================================================

os.chdir(       gloPar.dir['plots'] )
#pylab.savefig(  plotFile, dpi = dPar['dpi'])















