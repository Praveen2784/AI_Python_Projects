import numpy as np

# Define the range and amount as NumPy arrays
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Element-wise addition and subtraction
print(a + b)
print(a - b)
print(a / b)
print(a * b)

# Matrix Multiplication
Matmul = a@b
Matmul1 = np.matmul(a,b)
Matmul2 = np.dot(a,b)

print(Matmul)
print(Matmul1)
print(Matmul2)


N = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
A = N.reshape(4,3)
print(A)
print(A[:,])
print(A[:,0])
print(A[:,1])
print(A[:,2])
print(A[0,:])
print(A[1,:])
print(A[2,:])
print(A[3,:])
n,m = np.shape(A)

print(n,m)


