#python2.7 -*- coding: utf-8 -*-
"""
- test for variable type and return string
- test sign of number
"""
import numpy as np


def var_type( var):
    """
    :param var: some variable of unknown type
    :return: type of variable
    """
    if isinstance( var, float):
        strOut = 'type float'
    elif isinstance( var, int):
        strOut = 'type float'
    elif isinstance( var, np.ndarray):
        strOut = 'array of length %i'%( len( var))
    elif isinstance( var, list):
        strOut = 'list of length %i'%( len( var))
    else:
        strOut = 'unknown type'
    return strOut
print var_type( 3.4)
print var_type( [1,2,3,4,5])
print var_type( np.array([1,2,3,4,5]))


def var_sign( var):
    """
    test sign of number
    :param var: - some variable with unknow sign
    :return:
    """
    # in theory you can modify var_type to make sure var is not a list or array
    if var > 0:
        curr_sign = 'positive'
    elif var < 0:
        curr_sign = 'negative'
    else:
        curr_sign = 'var is equal 0'
    return curr_sign


print var_sign( -1)


print var_sign( 2)