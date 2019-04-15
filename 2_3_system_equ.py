"""
- solve linear systems of equations using np.linalg.solve

 example taken from: https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html

     3 * x0 +     x1 = 9
         x0 + 2 * x1 = 8:
    solution: x0 = 2, x1 = 3,
       since: x0 = 8-2x1; -5x1 = 9-24
"""
import numpy as np

# coeffiicient matrix: A
A = np.array([[3,1],
              [1,2]])
# solution vector: b
b = np.array([9,8])

# solve for Ax = b, using x = A^-1 b
x = np.dot(np.linalg.inv( A),b)
#or
x2  = np.linalg.solve( A, b)

print( x)
print( x2)