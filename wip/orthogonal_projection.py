import numpy as np

# Define a vector to project
v = np.array([3, 4, 0], dtype=np.float64)

# Define a basis for the subspace
u1 = np.array([1, 0, 0], dtype=np.float64)
u2 = np.array([0, 1, 0], dtype=np.float64)

# Compute the projection of v onto the subspace spanned by u1 and u2
proj_v = np.dot(v, u1) * u1 + np.dot(v, u2) * u2

# Compute the component orthogonal to the subspace
orth_component = v - proj_v

# Print the result
print("-" * 50)
print("Vector v:")
print(v)
print("\nBasis vectors for subspace:")
print(f"  u1 = {u1}")
print(f"  u2 = {u2}")
print("-" * 50)
print("Projection of v onto subspace:")
print(proj_v)
print("\nOrthogonal component:")
print(orth_component)
print("\nVerification: proj_v + orth_component = v")
print(np.allclose(proj_v + orth_component, v))
print("=" * 50)
