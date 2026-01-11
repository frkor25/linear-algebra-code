import numpy as np

# Define a vector
v = np.array([3, 4])

# Compute the norm (magnitude)
norm = np.linalg.norm(v)

# Normalize the vector
normalized_v = v / norm

# Print the result
print("-" * 50)
print("Vector v:")
print(v)
print("-" * 50)
print("Norm (magnitude) of v:", norm)
print("\nNormalized vector:")
print(normalized_v)
print("\nVerification (norm of normalized vector):", np.linalg.norm(normalized_v))
print("=" * 50)
