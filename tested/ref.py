import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[1, 2,  3,  4],
              [ 0,  0, 1, 2]])

# Compute the REF
sympy_matrix_pre_ref = Matrix(A)                                # 1. Convert NumPy array to SymPy Matrix
matrix_post_ref = sympy_matrix_pre_ref.echelon_form()           # 2. Compute REF using SymPy
numpy_ref_matrix = np.array(matrix_post_ref, dtype=np.float64)  # 3. Convert back to NumPy array

# Print the REF matrix
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("REF of matrix A:")
print(numpy_ref_matrix)                                                                       
print("=" * 50)