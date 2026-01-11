import numpy as np
from sympy import Matrix

# Define the coefficient matrix A and constant vector b
# System: 2x + 3y + z = 11
#         x - y + 2z = 8
#         3x + y - z = 6
A = np.array([[2, 3, 1],
              [1, -1, 2],
              [3, 1, -1]])

b = np.array([11, 8, 6])

# Solve using NumPy
x = np.linalg.solve(A, b)

# Print the result
print("-" * 50)
print("Coefficient matrix A:")
print(A)
print("\nConstant vector b:")
print(b)
print("-" * 50)
print("Solution x:")
print(x)
print("=" * 50)
