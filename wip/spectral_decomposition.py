import numpy as np
from sympy import Matrix

# Define a symmetric matrix A as a NumPy array
A = np.array([[4, 1],
              [1, 3]], dtype=np.float64)

# Convert to SymPy Matrix
sympy_matrix = Matrix(A)

# Compute eigenvalues and eigenvectors
eigenvals = sympy_matrix.eigenvals()
eigenvects = sympy_matrix.eigenvects()

# Spectral decomposition: A = sum(λ_i * v_i * v_i^T)
print("-" * 50)
print("Symmetric matrix A:")
print(A)
print("-" * 50)
print("Spectral Decomposition: A = Σ(λ_i · v_i · v_i^T)")
print("-" * 50)

spectral_sum = np.zeros_like(A, dtype=np.float64)

for eigenval, multiplicity, eigenvecs in eigenvects:
    eigenval_float = float(eigenval)
    for eigenvec in eigenvecs:
        # Convert eigenvector to NumPy array
        v = np.array(eigenvec, dtype=np.float64).flatten()
        # Normalize
        v = v / np.linalg.norm(v)
        # Add to spectral decomposition
        spectral_sum += eigenval_float * np.outer(v, v)
        print(f"λ = {eigenval}, v = {v}")
        print(f"λ · v · v^T =")
        print(eigenval_float * np.outer(v, v))
        print()

print("-" * 50)
print("Reconstructed matrix A (from spectral decomposition):")
print(spectral_sum)
print("\nVerification:")
print(np.allclose(A, spectral_sum))
print("=" * 50)
