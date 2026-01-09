import numpy as np

# Define the matrix A as a NumPy array
A = np.array([[1, 1, 0],
              [1, 0, 1],
              [0, 1, 1]], dtype=np.float64)

# Compute QR decomposition using NumPy
Q, R = np.linalg.qr(A)

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Orthonormal matrix Q:")
print(Q)
print("-" * 50)
print("Upper triangular matrix R:")
print(R)
print("-" * 50)
print("Verification: Q @ R = A")
print(np.allclose(Q @ R, A))
print("=" * 50)
