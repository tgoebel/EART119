#!python2.7
"""
Write a script that computes the annual rate of return and the absolute return on an investment of $1,000 at 10% over 30 years
 - lessons in compounding interest

"""
#===================================================================================
#                                params
#===================================================================================
iniInvest = 1e4
interest  = .1
nYears    = 30


#===================================================================================
#                                calculation
#===================================================================================
def invest_return( iniInvest, interest, nYears):
    currInvest = iniInvest
    for i in range( nYears):
        growth     = currInvest*.1
        currInvest += growth
        print( 'Year: %i, abs savings: %8.2f, rate of ini.: %4.3f'%( i+1, currInvest, (growth)/iniInvest))
        #print( 'Year: {x:d}, abs savings: {y:8.2f}, rate of ini.: {z:4.3f}'.format(  x=i+1, y=currInvest, z=(growth)/iniInvest))
        #print( 'Year: {0}, abs savings: {1}, rate of ini.: {2}'.format(  i+1, currInvest, (growth)/iniInvest))
    return currInvest

totSavings1  =invest_return( iniInvest, interest, nYears)
print 'total savings: ', totSavings1

# formula for total savings in year n
totSavings = (1 + interest)**nYears*iniInvest
print( 'total savings: {x:.2f}'.format( x=totSavings))
