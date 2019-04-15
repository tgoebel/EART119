#python2.7
"""
    use the dot product to compute mean and std of a data matrix m_Data

    - use numpy.random to create a 10x12 matrix of random numbers drawn from
      a normal distribution with mu and std

"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#===================================================================================
#                                params
#===================================================================================
# mean and standard deviation
iWells = 10
iMeas  = 12

a_mu_syn   = np.random.randint( 1, 40, iWells)*1.1 # mean pressure in MPa
a_std_syn  = np.random.randint( 1, 20, iWells)*.1  # stdev in MPa
#===================================1===============================================
#                            create synthetic pressure data
#===================================================================================

m_Data = a_mu_syn[0] + a_std_syn[0]*np.random.randn( iMeas)
for i in range( 1, iWells):
     m_Data = np.vstack( ( m_Data, a_mu_syn[i] + a_std_syn[i]*np.random.randn( iMeas)))

#plt.hist( m_Data.flatten(), 20)
#plt.show()

#===================================2===============================================
#                             computations
#===================================================================================
# mean
a_mean = np.dot( m_Data, np.ones( iMeas, dtype = float).reshape(iMeas,1))/iMeas
#a_mean = np.dot( m_Data, np.ones( iWells, dtype = float).reshape(-1,1)/iMeas
print( 'meas pressure: ', np.round( a_mean.flatten(), 1))
print( 'input pres,  : ', a_mu_syn)

m_diff = (m_Data - np.dot( a_mean.reshape( iWells, 1), np.ones( (1, iMeas), dtype = float)))
squared_diff = m_diff*m_diff
a_std  = ( np.dot( squared_diff, np.ones( iMeas).reshape(-1, 1))/iMeas)**(1/2)

print( 'input std.: ', a_std_syn)
print( 'meas. std.: ', np.round( a_std.flatten(), 1))

#  numpy solution
#print np.round( m_Data.std( axis = 1), 1)





