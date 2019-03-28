#!python2.7
"""
- compute pi using Leibniz method and compare to true value from python math


"""
import math


def my_pi( N):
    sum_pi = 0
    for i in range( N):
        sum_pi += 1./( ( 4*i+1) * (4*i+3))
    return 8*sum_pi

for N in [10, 50, 100, 1000]:
    fMyPi = my_pi( N)
    print 'my pi', fMyPi, 'err: ', math.pi-fMyPi