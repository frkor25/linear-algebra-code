import numpy as np

# Define the matrix A
A = np.array([[1, 3],
              [-2, -1],
              [1, -3],
              [0, 4]])

# Define the vector x
x = np.array([[2],
              [1]])

# Perform matrix-vector multiplication
result = A @ x

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Vector x:")
print(x)
print("-" * 50)
print("Result of A @ x:")
print(result)
print("=" * 50)
