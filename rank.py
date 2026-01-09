import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[-2, -4,  2,  2],
              [ 0,  0, -2, -4],
              [ 0,  0,  0,  0]])

# Convert NumPy array to SymPy Matrix
sympy_matrix = Matrix(A)

# Compute the rank using SymPy
rank = sympy_matrix.rank()

# Print the result
print("-" * 50)
print("Matrix:")
print(A)
print("\nRank of the matrix:", rank)
print("=" * 50)