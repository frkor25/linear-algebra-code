# lambda n bliver ikke lavet automatisk i denne fil der er kun 2. rækkefølgen er heller ikke på plads



import numpy as np
from sympy import Matrix

# Define the matrix A as a NumPy array
A = np.array([[2, 0, 0],
              [1, 2, -1],
              [1, 3, -2]])

# Convert NumPy array to SymPy Matrix
sympy_matrix = Matrix(A)

# Compute eigenvalues and eigenvectors using SymPy
eigenvals = sympy_matrix.eigenvals()
eigenvects = sympy_matrix.eigenvects()

# Extract and sort eigenvalues for λ₁ and λ₂
eigenval_list = sorted(eigenvals.keys())
lambda_1 = eigenval_list[0]
lambda_2 = eigenval_list[1]

# Print the result
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)
print("Eigenvalues:")
print(f"  λ₁ = {lambda_1}")
print(f"  λ₂ = {lambda_2}")
print("-" * 50)
print("Eigenvectors:")
for eigenval, multiplicity, eigenvecs in eigenvects:
    if eigenval == lambda_1:
        print(f"  For λ₁ = {lambda_1}:")
        for eigenvec in eigenvecs:
            print(f"    v₁ = {eigenvec.T}")
    elif eigenval == lambda_2:
        print(f"  For λ₂ = {lambda_2}:")
        for eigenvec in eigenvecs:
            print(f"    v₂ = {eigenvec.T}")
print("=" * 50)
