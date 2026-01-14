import numpy as np

# Define the matrix A as a NumPy array
A = np.array([[7, 6],
              [6, -2]])

# Define a potential eigenvector
v = np.array([-1, 2])

# Check if v is an eigenvector of A
# A vektor v is an eigenvector of A if A @ v = λ * v for some scalar λ

# Compute A @ v
A_v = A @ v

# Check if A @ v is proportional to v
# If v is an eigenvector, then A @ v should be parallel to v
# We check if A @ v = λ * v for some λ

is_eigenvector = False
eigenvalue = None

# Find the first non-zero component of v to calculate λ
for i in range(len(v)):
    if v[i] != 0:
        lambda_candidate = A_v[i] / v[i]
        # Check if A @ v = λ * v for all components
        if np.allclose(A_v, lambda_candidate * v):
            is_eigenvector = True
            eigenvalue = lambda_candidate
        break

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("\nVector v:")
print(v)
print("-" * 50)
print("A @ v:")
print(A_v)
print("-" * 50)
if is_eigenvector:
    print(f"v is an EIGENVECTOR of A with eigenvalue λ = {eigenvalue}")
else:
    print("v is NOT an eigenvector of A")
print("=" * 50)
