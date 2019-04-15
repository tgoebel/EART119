# -*- coding: utf-8 -*-
# python 2.7
'''
Created on April 13, 2019

    - some examples on how indexing works in a for loop and for arrays

@author: tgoebel
'''
import numpy as np
### variables
aX = np.arange( 20, 31, 1)
print( 'this is the data vector', aX)


#### Indexing#######
print(' every second element')
aID= np.arange(0 , 10+2, 2)
print( aX[aID])

print( '  last three elements')
print( aX[-3::])

print(' first 2 and last two vector entries')
print( np.hstack( (aX[0:2], aX[-2::])))

# second data vector
aY = np.arange( 40, 51, 1)

print( 'sum even and odd elements')
sum = 0
for i in np.arange(1, 10, 2, dtype = int):
    print i, aX[i-1], aY[i]
    sum += aX[i-1] + aY[i]
print( 'sum even + odd in for loop', sum)

##vectorize the sum
iEven  = np.arange(0, 10, 2, dtype = int)
iOdd   = iEven + 1
#print iEven, iOdd
print( 'sum vectorized', np.dot( aX[iEven]+aY[iOdd], np.ones( len(iOdd))))
## or just use sum() from numpy
print( 'sum vectorized', ( aX[iEven]+aY[iOdd]).sum())
