import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[1, 4, 2],
              [0, 0, 1],
              [0, 0, 0]])

# Convert NumPy array to SymPy Matrix
sympy_matrix = Matrix(A)

# Compute RREF to identify pivot columns
rref_matrix, pivot_cols = sympy_matrix.rref()

# Get dimensions
rows, cols = A.shape

# Identify leading and free variables
leading_variables = []
free_variables = []

for col in range(cols):
    if col in pivot_cols:
        leading_variables.append((col, f"x{col+1}"))
    else:
        free_variables.append((col, f"x{col+1}"))

# Print the results
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("RREF of Matrix A:")
print(np.array(rref_matrix, dtype=np.float64))
print("-" * 50)
print("LEADING VARIABLES (Pivot columns):")
if leading_variables:
    for col, var in leading_variables:
        print(f"  {var} at column {col+1}")
else:
    print("  None")
print("-" * 50)
print("FREE VARIABLES (Non-pivot columns):")
if free_variables:
    for col, var in free_variables:
        print(f"  {var} at column {col+1}")
else:
    print("  None")
print("=" * 50)
