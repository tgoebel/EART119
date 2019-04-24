#!/bin/python2.7
"""
--> exponential function that describe radio active decay

"""
import numpy as np

#------------------------------------------------------------------------
#                   params
#------------------------------------------------------------------------
a_tau = np.array([5730-40, 5730, 5730+40])
at = np.array([10*1e3, 100*1e3, 1e6])

#----------------------------1-------------------------------------------
#                    function
#------------------------------------------------------------------------
def radio_decay( time, tau, N0=None):
    """

    :param time: - time since start of decay (e.g. surface exposure)
    :param tau:  - half-life
    :param N0:   - initial quantity of substance
    :return:
    """
    if N0 == None:
        N0 = 1 # to compute fractional amount remaining
    return N0*np.exp( -time/tau)
#----------------------------2-------------------------------------------
#                   computation
#------------------------------------------------------------------------
for time in at:
    print 't since t0', time, 'percent substance remaining', radio_decay(time, a_tau)*100


# substance remaining from input
print 'Enter Time since t0 in yr'
time = input()
print 'Enter Half Life of substance'
tau = input()

print 't since t0', time, 'percent substance remaining', radio_decay(time, tau1e6)*100



