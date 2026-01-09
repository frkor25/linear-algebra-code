import numpy as np

# Define a set of linearly independent vectors
v1 = np.array([1, 1, 0], dtype=np.float64)
v2 = np.array([1, 0, 1], dtype=np.float64)
v3 = np.array([0, 1, 1], dtype=np.float64)

vectors = np.array([v1, v2, v3]).T

# Perform Gram-Schmidt orthogonalization
u_vectors = []

for i in range(vectors.shape[1]):
    u = vectors[:, i].copy()
    
    for j in range(i):
        u = u - np.dot(u_vectors[j], vectors[:, i]) * u_vectors[j]
    
    u_norm = np.linalg.norm(u)
    u_normalized = u / u_norm
    u_vectors.append(u_normalized)

orthonormal_basis = np.array(u_vectors).T

# Print the result
print("-" * 50)
print("Original vectors:")
for i, vec in enumerate([v1, v2, v3], 1):
    print(f"  v{i} = {vec}")
print("-" * 50)
print("Orthonormal basis (Gram-Schmidt):")
for i, vec in enumerate(u_vectors, 1):
    print(f"  e{i} = {vec}")
print("-" * 50)
print("Verification (orthogonality):")
for i in range(len(u_vectors)):
    for j in range(i + 1, len(u_vectors)):
        dot_product = np.dot(u_vectors[i], u_vectors[j])
        print(f"  e{i} · e{j} = {dot_product:.10f}")
print("=" * 50)
