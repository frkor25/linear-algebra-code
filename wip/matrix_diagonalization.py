import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[1, 0, 1],
              [0, 1, 0],
              [0, 0, -3]], dtype=np.float64)

# Convert to SymPy Matrix
sympy_matrix = Matrix(A)

# Compute diagonalization: A = P @ D @ P^(-1)
P, D = sympy_matrix.diagonalize()

# Convert to NumPy arrays
numpy_P = np.array(P, dtype=np.float64)
numpy_D = np.array(D, dtype=np.float64)
numpy_P_inv = np.linalg.inv(numpy_P)

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Eigenvector matrix P:")
print(numpy_P)
print("-" * 50)
print("Diagonal matrix D:")
print(numpy_D)
print("-" * 50)
print("Verification: A = P @ D @ P^(-1)")
print(np.allclose(A, numpy_P @ numpy_D @ numpy_P_inv))
print("=" * 50)
