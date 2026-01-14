import numpy as np
from sympy import Matrix
from sympy.matrices.exceptions import NonInvertibleMatrixError
from fractions import Fraction

# Define the matrix A as a NumPy array
A = np.array([[2, 0, -1],
              [3, 1, 2],
              [-2, 4, -3]])

# Convert NumPy array to SymPy Matrix
sympy_matrix = Matrix(A)

# Print the matrix
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)

# Check determinant first
det = sympy_matrix.det()
print(f"Determinant: {det}")
print("-" * 50)

# Try to compute the inverse
try:
    matrix_inverse = sympy_matrix.inv()
    
    # Convert to NumPy array for decimal display
    numpy_inverse = np.array(matrix_inverse, dtype=np.float64)
    
    print("Inverse of A (Decimal):")
    print(numpy_inverse)
    print("-" * 50)
    print("Inverse of A (Fraction):")
    for i in range(matrix_inverse.shape[0]):
        row = []
        for j in range(matrix_inverse.shape[1]):
            element = matrix_inverse[i, j]
            # Convert to fraction
            frac = Fraction(str(element)).limit_denominator(1000)
            row.append(str(frac))
        print("  [ " + ", ".join(f"{f:>6}" for f in row) + " ]")
    
except NonInvertibleMatrixError:
    print("ERROR: Matrix is NOT invertible (singular)")
    print("Reason: Determinant is 0")
    print("The matrix rows/columns are linearly dependent.")

print("=" * 50)
