import numpy as np
from sympy import Matrix
from fractions import Fraction

# Define the matrix A as a NumPy array
A = np.array([[1, 0, -1],
              [-1, 1, 0],
              [0, -4, 1]])

# Convert NumPy array to SymPy Matrix
sympy_matrix = Matrix(A)

# Print the matrix
print("-" * 50)
print("Matrix A:")
print(A)
print("-" * 50)

# Compute the adjugate (adjoint) matrix
adjugate = sympy_matrix.adjugate()

# Convert to NumPy array for decimal display
numpy_adjugate = np.array(adjugate, dtype=np.float64)

print("Adjugate of A (Decimal):")
print(numpy_adjugate)
print("-" * 50)

print("Adjugate of A (Fraction):")
for i in range(adjugate.shape[0]):
    row = []
    for j in range(adjugate.shape[1]):
        element = adjugate[i, j]
        # Convert to fraction
        frac = Fraction(str(element)).limit_denominator(1000)
        row.append(str(frac))
    print("  [ " + ", ".join(f"{f:>6}" for f in row) + " ]")

print("=" * 50)

# Verification: A * adj(A) = det(A) * I
det = sympy_matrix.det()
det_float = float(det)
identity = np.eye(A.shape[0])

product = np.dot(A, numpy_adjugate)
expected = det_float * identity

print("Verification: A × adj(A) = det(A) × I")
print(f"Determinant: {det_float}")
print("\nA × adj(A):")
print(product)
print(f"\ndet(A) × I = {det_float} × I:")
print(expected)
print("\nEqual?", np.allclose(product, expected))

print("=" * 50)

# Relationship with inverse: adj(A) = det(A) * A^(-1)
if det_float != 0:
    inverse = sympy_matrix.inv()
    numpy_inverse = np.array(inverse, dtype=np.float64)
    adjugate_from_inverse = det_float * numpy_inverse
    
    print("Relationship: adj(A) = det(A) × A⁻¹")
    print("\ndet(A) × A⁻¹:")
    print(adjugate_from_inverse)
    print("\nMatches adj(A)?", np.allclose(numpy_adjugate, adjugate_from_inverse))
else:
    print("Matrix is singular (det = 0), inverse does not exist")
    print("But adjugate still exists!")

print("=" * 50)
