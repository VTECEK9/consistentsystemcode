from numpy import array, zeros 
import numpy as np

a = np.array([[1,-7, 0,6], [0, 0, 1,-2], [-1,7,-4,2] ], float)
b = np.array([5,-3,7], float)
n = len(b)
x = zeros(n,float)
#row reduction
for k in range(n-1):
    for i in range(k+1,n):
        if a[i,k] == 0:continue
        factor = a[k,k]/a[i,k]
        for j in range(k,n):
            a[i,j] = a[k,j] - a[i,j]*factor
        b[i] = b[k] - b[i]*factor
c = np.c_[a,b]
print(c)

#checks if matrix is consistent, IE: last row is all zeros except last element 
rows = c.shape[0]

cols = c.shape[1]

for i in range(0, rows):
    zero = False
    rowZero = True
    for j in range(0, cols):
        if (j==cols-1) and rowZero == True and c[i,j] != 0:
                print("The matrix is inconsistent")
        if c[i,j] == 0:
            zero = True
        else: rowZero = False
        zero = False
        
        
