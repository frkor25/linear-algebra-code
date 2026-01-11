import numpy as np

# Define two boolean matrices
A = np.array([[True, True, False],
              [True, False, True],
              [False, True, False]])

B = np.array([[True, True, False],
              [True, False, True],
              [False, True, False]])

# Compute the boolean product: C[i,j] = OR(AND(A[i,k], B[k,j]))
rows_A, cols_A = A.shape
rows_B, cols_B = B.shape

if cols_A != rows_B:
    print("Error: incompatible matrix dimensions for boolean product")
else:
    C = np.zeros((rows_A, cols_B), dtype=bool)
    
    for i in range(rows_A):
        for j in range(cols_B):
            # Boolean product: OR of all AND operations
            C[i, j] = np.any(np.logical_and(A[i, :], B[:, j]))

# Print the result
print("-" * 50)
print("Matrix A:")
print(A.astype(int))
print("\nMatrix B:")
print(B.astype(int))
print("-" * 50)
print("Boolean Product A ⊙ B:")
print(C.astype(int))
print("=" * 50)
