# Shape and Reshape in numpy
import numpy as np
a = np.array([1,2,3,4,5,6,7,8])
print(a)
b = a.reshape(2,2,2)
print(b)


# concatenate
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = np.concatenate((a,b),axis=1)
print(c)

# Stack
a = [1,2,3,4]
b = [5,6,7,8]
c = np.stack((a,b),axis=1)
print(c)

# Hstack
a = [1,2,3,4]
b = [5,6,7,8]
c = np.hstack((a,b))
print(c)

# vstack
a = [1,2,3,4]
b = [5,6,7,8]
c = np.vstack((a,b))
print(c)

# copy
a = np.array([1,2,3,4])
b = a.copy()
a[0]=10
print(a)
print(b)

# view
a = np.array([1,2,3,4])
b = a.view()
a[0]=10
print(a)
print(b)

