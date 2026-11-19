import numpy as np
a = np.arange(5,126,5)
b = a.reshape(5,5)
print("2D Matrix:")
print(b)
print("Number of dimensions:",b.ndim)
print("Shape of the matrix:",b.shape)
print("The total number of elements", b.size)
print("Data type of the element:",b.dtype)
