import numpy as np

# Define two 3D vectors
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

# Compute the cross product
cross_product = np.cross(u, v)

# Print the result
print("-" * 50)
print("Vector u:")
print(u)
print("\nVector v:")
print(v)
print("-" * 50)
print("Cross product u × v:")
print(cross_product)
print("=" * 50)
