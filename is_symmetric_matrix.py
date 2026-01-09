import numpy as np

# Define the matrix A as a NumPy array
A = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, 6]])

# Check if the matrix is symmetric
is_symmetric = np.allclose(A, A.T)

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Transpose of A:")
print(A.T)
print("-" * 50)
print("Is matrix symmetric?", is_symmetric)
print("=" * 50)
