import numpy as np

# Define the matrix A as a NumPy array
A = np.array([[1, 0, 1],
              [0, 1, 2]])

# Define the matrix B as a NumPy array
B = np.array([[4, 2, 12],
              [10, 6, 4]])

# Perform matrix subtraction
result = A - B

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-")
print("Matrix B:")
print(B)
print("-" * 50)
print("Result of A - B:")
print(result)
print("=" * 50)
