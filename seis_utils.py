"""

 utility functions to analyze earthquake data sets

"""
from __future__ import division
import numpy as np

#===================================================================================
#                         rate computation
#===================================================================================
def eqRate( at, k_win):
    # smoothed rate from overlapping sample windows normalized by delta_t
    aS          = np.arange( 0, at.shape[0]-k_win, 1)
    aBin, aRate = np.zeros(aS.shape[0]), np.zeros(aS.shape[0])
    iS = 0
    for s in aS:
        i1, i2 = s, s+k_win
        aBin[iS]  = 0.5*( at[i1]+at[i2])
        aRate[iS] = k_win/( at[i2]-at[i1])
        iS += 1
    return aBin, aRate



#===================================================================================
#                         time and distance
#===================================================================================

def haversine( lon1, lat1, lon2, lat2, **kwargs):
    """
    haversine formula implementation
    https://en.wikipedia.org/wiki/Great-circle_distance
    great circle distance between two points
    :input   lon1, lat1
             lon2, lat2

    		  gR - Earth radius (global variable)
    :output  distance - great circle distance in meter
    """
    gR = 6371 #6378.137 #?
    # convert to radians
    lon1 = lon1 * np.pi / 180
    lon2 = lon2 * np.pi / 180
    lat1 = lat1 * np.pi / 180
    lat2 = lat2 * np.pi / 180
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    distance = gR * c
    return distance

def dateTime2decYr( YR, MO, DY, HR, MN, SC):
    """
    - convert date time to decimal year
    :param YR: - int or arrays
    :param MO:
    :param DY:
    :param HR:
    :param MN:
    :param SC:
    :return:
    """
    nDays = 365.25
    return YR + (MO-1)/12 + (DY-1)/nDays  + HR/(nDays*24) + MN/(nDays*24*60) + SC/(nDays*24*3600)


def area_poly_vec( aX, aY):
    """
    use:

    A = 0.1*abs( (x1*y2 + x2*y3 + xn-1*yn + xn*y1) - (y1*x2 + y2*x3 + ... + yn-1*xn + yn*x1))
    :param aX: - x-coordinates of all vertices
    :param aY: - y-coordinates of all vertices
    :return: A - area of polygon
    """
    sumVert1 = (aX[0:-1]*aY[1::]).sum()+aX[-1]*aY[0]
    sumVert2 = (aY[0:-1]*aX[1::]).sum()+aY[-1]*aX[0]
    # or
    #sum = (aX[0:-1]*aY[1::] - aY[0:-1]*aX[1::]).sum() + (aX[-1]*aY[0]-aY[-1]*aX[0])
    return 0.5*abs( sumVert1 - sumVert2)