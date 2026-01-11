import numpy as np
from sympy import Matrix

# Define the coefficient matrix (A) and constant matrix (b) / constant vector (b)

A = np.array([[1, 3, 1, 1],
              [2, -2, 1, 2],
              [3, 1, 2, -1]])

b = np.array([[-3],
              [-8],
              [-1]])

# Rest of your code remains the same...
A_augmented = np.hstack([A, b])
sympy_coeff = Matrix(A)
sympy_augmented = Matrix(A_augmented)

rref_augmented, pivot_cols_augmented = sympy_augmented.rref()
rref_augmented_array = np.array(rref_augmented, dtype=np.float64)

rank_coeff = sympy_coeff.rank()
rank_augmented = sympy_augmented.rank()
num_variables = A.shape[1]

print("-" * 50)
print("Coefficient Matrix A:")
print(A)
print("-" * 50)
print("Constant Vector b:")
print(b)
print("-" * 50)
print("Augmented Matrix [A | b]:")
print(A_augmented)
print("-" * 50)
print("RREF of Augmented Matrix:")
print(rref_augmented_array)
print("-" * 50)
print(f"Rank of coefficient matrix: {rank_coeff}")
print(f"Rank of augmented matrix: {rank_augmented}")
print(f"Number of variables: {num_variables}")
print("-" * 50)

# Check for inconsistency
inconsistent = False
for row in range(len(rref_augmented_array)):
    if np.allclose(rref_augmented_array[row, :-1], 0) and not np.isclose(rref_augmented_array[row, -1], 0):
        inconsistent = True
        break

if inconsistent:
    print("The system has NO SOLUTION (Inconsistent)")
elif rank_coeff == rank_augmented == num_variables:
    print("The system has ONE UNIQUE SOLUTION")
    print("\n✓ CONSISTENT - Unique Solution:")
    for i in range(num_variables):
        solution_value = rref_augmented_array[i, -1]
        print(f"  x{i+1} = {solution_value}")
elif rank_coeff == rank_augmented < num_variables: 
    num_free = num_variables - rank_coeff
    print(f"The system has INFINITE SOLUTIONS ({num_free} free variable(s))")

print("=" * 50)