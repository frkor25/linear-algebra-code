import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[4, 7],
              [2, 6]])

# Convert NumPy array to SymPy Matrix
sympy_matrix = Matrix(A)

# Compute the determinant using SymPy
determinant = sympy_matrix.det()

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Determinant of A:", determinant)
print("=" * 50)
