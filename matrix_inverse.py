import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[4, 7],
              [2, 6]])

# Convert NumPy array to SymPy Matrix
sympy_matrix = Matrix(A)

# Compute the inverse using SymPy
matrix_inverse = sympy_matrix.inv()

# Convert back to NumPy array
numpy_inverse = np.array(matrix_inverse, dtype=np.float64)

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Inverse of A:")
print(numpy_inverse)
print("=" * 50)
