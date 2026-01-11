import numpy as np

# Define the matrix A as a NumPy array
A = np.array([[2, -4],
              [-1, -1]])

# Define the eigenvalue to check
eigenvalue = 3

# Create identity matrix of the same size as A
I = np.eye(A.shape[0])

# Compute A - λI
A_minus_lambda_I = A - eigenvalue * I

# Compute determinant
determinant = np.linalg.det(A_minus_lambda_I)

# Check if determinant is close to zero (tolerance for numerical errors)
is_eigenvalue_result = np.abs(determinant) < 1e-9

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print(f"\nEigenvalue candidate: λ = {eigenvalue}")
print("-" * 50)
print(f"A - λI =")
print(A_minus_lambda_I)
print("-" * 50)
print(f"det(A - λI) = {determinant:.10f}")
print(f"\nIs λ = {eigenvalue} an eigenvalue of A? {is_eigenvalue_result}")
print("=" * 50)
