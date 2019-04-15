#python2.7
"""
    -  compute that cross-over point between two discrete fct. f(x) and g(x)
"""
import numpy as np
import matplotlib.pyplot as plt
#===================================================================================
#                                params
#===================================================================================
tmin, tmax = -10, 10
f_dt = 1e-2
iN = int( (tmax-tmin)/f_dt)

t0 = 2.5
c  = 1.1
A  = 7
eps= 1e-1
testPlot = True
#===================================================================================
#                                define fct.
#===================================================================================

def f_t( t, c, t0):
    return c*(t - t0)**2

def g_t( t, A):
    return A*t + t0

def g2_t( t, A, t0):
    return A*t**2 + t0
#===================================================================================
#                          find cross-over point: for loop
#===================================================================================
#A# for loop
f_curr_t = tmin
for i in range( iN):
    f_curr_t += f_dt
    f_curr_gt = g_t( f_curr_t, A)
    f_curr_ft = f_t( f_curr_t, c, t0)
    #print abs( f_curr_fx - f_curr_gx)
    if abs( f_curr_ft - f_curr_gt) < eps:
        print( 'cross-over point at t=%.2f, g(t) = %.2f, f(t) = %.2f'%( f_curr_t,f_curr_gt, f_curr_ft))

#===================================================================================
#                          find cross-over point: vectorized
#===================================================================================
a_t = np.linspace( tmin, tmax, iN)
## vectorized solution
a_ft  = f_t(  a_t, c, t0)
a_gt  = g_t(  a_t, A)
a_g2t = g2_t( a_t, A, t0)

#B#
a_df_g  = a_ft - a_gt
a_df_g2 = a_ft - a_g2t
## find all cross-over points
sel = abs(a_df_g) < eps
print 'all cross-over points:, ',a_t[sel], a_ft[sel], a_g2t[sel]
## find minimum between fx - gx
sel_min = abs( a_df_g) == abs(a_df_g).min() # this results in a boolean array of 1 and 0
print 'cross over with min. distance: t=%s, f(t)=%s, g(t)=%s'%( a_t[sel_min], a_ft[sel_min], a_g2t[sel_min])

## test plot
if testPlot == True:
    # plt.plot( a_t, abs(a_df_g),  'o', mec = 'r', ms = 2, mfc = 'none', label = '|f - g|')
    # plt.plot( a_t, abs(a_df_g2), 'o', mec = 'b', ms = 2, mfc = 'none', label = '|f - g2|')
    # plt.plot( [tmin, tmax], [0,0], 'k--')
    # plt.xlabel( 't')
    # plt.ylabel( 'Error Function')

    plt.plot( a_t, f_t( a_t, c, t0), 'o', mec = 'r', ms = 2, mfc = 'none', label = 'f(t)')
    plt.plot( a_t, g_t( a_t, A), 'o',     mec = 'b', ms = 2, mfc = 'none',  label = 'g(t)')
    #plt.plot( a_t, g2_t( a_t, A, t0), 'o', mec = 'g', ms = 2, mfc = 'none',  label = 'g2(t)')
    plt.xlabel( 'f(t)')
    plt.ylabel( 'g(t)')
    plt.legend()
    plt.show()