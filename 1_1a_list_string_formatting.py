'''
Created on Feb 23, 2017

- split, strip strigns
- modify lists in place or create new list using online for loops and if statement

@author: tgoebel
'''
#--------------------------------------------------------

my_str1 = '001 gsfg 2541.0000'

print( my_str1[0:3])
print( my_str1.strip('0'))
print( my_str1.split('.'))
print( my_str1.split('1'))
print( int( my_str1.split('.')[-1]))
print( my_str1.replace( 'g', '1'))
lStr = [my_str1[i] for i in range(len(my_str1))]
print( 'create list of every string entry')
print( lStr)

#--------------------------------------------------------
my_str2 = 'gsfg254ggfsg'
lList = [my_str2[i] for i in range( len(my_str2))]
newList = [x.replace('g', '5') for x in lList]
print( '5 instead of g')
print( newList)
print( 'find all 5s and add 2')
lList7 = [int(x)+2 for x in lList if x == '5']
print( lList7)
lID5 = [i for i in range( len( lList)) if lList[i] == '5']
print( lList, lID5)













