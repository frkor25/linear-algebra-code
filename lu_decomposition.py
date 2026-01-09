import numpy as np
from scipy.linalg import lu

# Define the matrix A as a NumPy array
A = np.array([[4, 3, 2],
              [6, 3, 4],
              [3, 3, 5]], dtype=np.float64)

# Compute LU decomposition using SciPy
P, L, U = lu(A)

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Permutation matrix P:")
print(P)
print("-" * 50)
print("Lower triangular matrix L:")
print(L)
print("-" * 50)
print("Upper triangular matrix U:")
print(U)
print("-" * 50)
print("Verification: P @ A = L @ U")
print(np.allclose(P @ A, L @ U))
print("=" * 50)
