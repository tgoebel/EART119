#!/bin/python2.7
"""
--> compute area of basic geometries
--> radiactive decay

"""
import numpy as np

#------------------------------------------------------------------------
#                   params
#------------------------------------------------------------------------
# triangle
aX_tri = np.array([ 3, 2, 0])
aY_tri = np.array([ 1, 3, 1])
hb, b = 2, 3
# polygon
aX_poly= np.array([ 1, 3, 4, 3.5, 2])
aY_poly= np.array([ 1, 1, 2, 5,   4])
# test case - pentagon with A = 5
#aX_poly = np.array([0, 2, 2, 1, 0])
#aY_poly = np.array([0, 0, 2, 3, 2])

#rectangle
aX_rec = np.array([ 0, 2, 2, 0])
aY_rec = np.array([ 0, 0, 3, 3])
#----------------------------1-------------------------------------------
#                   function
#------------------------------------------------------------------------

def area_circle( r):
    return np,pi*r**2

def area_rect( a,b):
    return a*b

def area_triangle(  b, h):
    return 0.5*h*b

def area_poly( aX, aY):
    """
    use:

    A = 0.1*abs( (x1*y2 + x2*y3 + xn-1*yn + xn*y1) - (y1*x2 + y2*x3 + ... + yn-1*xn + yn*x1))
    :param aX: - x-coordinates of all vertices
    :param aY: - y-coordinates of all vertices
    :return: A - area of polygon
    """
    # type testing for numpy arrays
    if isinstance( aX, (np.ndarray)) and isinstance( aY, (np.ndarray)):
        pass
    else:
        error_str = 'x or y or both are not np.arrays'
        raise ValueError, error_str
    ## solve within for loop
    n = aX.shape[0]# number of vertices
    sumVert1 = 0
    sumVert2 = 0
    for i in range( n-1):
        sumVert1 += aX[i]*aY[i+1]
        sumVert2 += aY[i]*aX[i+1]
        # sum += aX[i]*aY[i+1] - aY[i]*aX[i+1]
    # add last term
    sumVert1 += aX[-1]*aY[0]
    sumVert2 += aY[-1]*aX[0]
    return 0.5*abs( sumVert1 - sumVert2)

def area_poly_vec( aX, aY):
    """
    use:

    A = 0.1*abs( (x1*y2 + x2*y3 + xn-1*yn + xn*y1) - (y1*x2 + y2*x3 + ... + yn-1*xn + yn*x1))
    :param aX: - x-coordinates of all vertices
    :param aY: - y-coordinates of all vertices
    :return: A - area of polygon
    """
    #sumVert1 = (aX[0:-1]*aY[1::]).sum()+aX[-1]*aY[0]
    # or:
    sumVert1  = np.dot( aX[0:-1], aY[1::])+aX[-1]*aY[0]
    #sumVert2 = (aY[0:-1]*aX[1::]).sum()+aY[-1]*aX[0]
    # or:
    sumVert2  = np.dot(aY[0:-1], aX[1::])+aY[-1]*aX[0]
    #sum = (aX[0:-1]*aY[1::] - aY[0:-1]*aX[1::]).sum() + (aX[-1]*aY[0]-aY[-1]*aX[0])
    return 0.5*abs( sumVert1 - sumVert2)

#----------------------------2-------------------------------------------
#                   computation
#------------------------------------------------------------------------
print 'area rect: ', area_rect( (aX_rec[1]-aX_rec[0]), aY_rec[2]-aY_rec[1]),
print area_poly( aX_rec, aY_rec), area_poly_vec(aX_rec, aY_rec)
print 'area triangle', area_triangle( b, hb), area_poly( aX_tri, aY_tri), area_poly_vec(aX_tri, aY_tri)
print 'area polygon', area_poly( aX_poly, aY_poly), area_poly_vec(aX_poly, aY_poly)








