import numpy as np
from sympy import Matrix

# Define the augmented matrix [A | b]
# System: 2x + 3y + z = 11
#         x - y + 2z = 8
#         3x + y - z = 6
A = np.array([[1,  0],
              [0, 1]], dtype=np.float64)

# Convert to SymPy Matrix for row reduction
sympy_matrix = Matrix(A)

# Perform Gaussian elimination to row echelon form
row_echelon = sympy_matrix.rref()

# Extract the RREF matrix
rref_matrix = row_echelon[0]
numpy_rref = np.array(rref_matrix, dtype=np.float64)

# Print the result
print("-" * 50)
print("Augmented matrix [A | b]:")
print(A)
print("-" * 50)
print("Row Reduced Echelon Form:")
print(numpy_rref)
print("=" * 50)
