
import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[1, 2, 3, 4],
              [0, 0, 1, 2]])


# Compute the RREF
sympy_matrix_pre_rref = Matrix(A)                                   # 1. Convert NumPy array to SymPy Matrix
matrix_post_rref = sympy_matrix_pre_rref.rref()                     # 2. Compute RREF using SymPy  
rref_matrix = matrix_post_rref[0]                                   # 3. Extract the RREF matrix
numpy_rref_matrix = np.array(rref_matrix, dtype=np.float64)         # 4. Convert back to NumPy array

# Print the RREF matrix
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("REFF of matrix A:")
print(numpy_rref_matrix)                                                                          
print("=" * 50)

