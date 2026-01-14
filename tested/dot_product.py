import numpy as np

# Define two vectors
u = np.array( [5, 7, 1])
v = np.array([-2, -1, 3])

# Compute the dot product
dot_product = np.dot(u, v)

# Helper functions
def angle_degrees(a: np.ndarray, b: np.ndarray) -> float | None:
	"""Return the angle between vectors a and b in degrees.
	If either vector has zero norm, return None.
	"""
	na = np.linalg.norm(a)
	nb = np.linalg.norm(b)
	if na == 0 or nb == 0:
		return None
	cos_theta = np.dot(a, b) / (na * nb)
	# Numerical safety
	cos_theta = np.clip(cos_theta, -1.0, 1.0)
	return float(np.degrees(np.arccos(cos_theta)))

def classify_by_dot(d: float, tol: float = 1e-12) -> str:
	"""Classify angle via dot-product sign with tolerance."""
	if d > tol:
		return "acute (< 90°)"
	if d < -tol:
		return "obtuse (> 90°)"
	return "right (90°)"

def is_orthogonal(d: float, tol: float = 1e-12) -> bool:
	return abs(d) <= tol

# Compute additional metrics
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)
distance_uv = np.linalg.norm(u - v)

# Compute projection of u onto v
if norm_v != 0:
	proj_u_onto_v = (np.dot(u, v) / (norm_v ** 2)) * v
else:
	proj_u_onto_v = None

# Print the result
print("-" * 50)
print("Vector u:")
print(u)
print("\nVector v:")
print(v)
print("-" * 50)
print("Dot product u · v:", dot_product)
print("=" * 50)
print(f"||u|| (norm of u): {norm_u:.6f}")
print(f"||v|| (norm of v): {norm_v:.6f}")
print(f"Distance ||u - v||: {distance_uv:.6f}")
if proj_u_onto_v is not None:
	print("Projection of u onto v:")
	print(proj_u_onto_v)
else:
	print("Projection of u onto v: undefined (v is zero vector)")
print("=" * 50)
# Angle and classification
theta = angle_degrees(u, v)
if theta is not None:
	print(f"Angle between u and v: {theta:.3f}°")
else:
	print("Angle between u and v: undefined (zero vector involved)")
print("Classification:", classify_by_dot(dot_product))
print("Orthogonal (perpendicular)?:", is_orthogonal(dot_product))

# Key properties demonstration
print("-" * 50)
print("Properties check")
dot_uv = np.dot(u, v)
dot_vu = np.dot(v, u)
print("Commutative a·b = b·a:", dot_uv == dot_vu, f"({dot_uv} vs {dot_vu})")

# Create a vector w with the same dimension as u and v
w = np.ones(len(u)) * 2  # Example: all elements are 2
w[0] = 1  # Vary the first element for interest
left = np.dot(u, v + w)
right = np.dot(u, v) + np.dot(u, w)
print("Distributive a·(b+c) = a·b + a·c:", left == right, f"({left} vs {right})")
print("=" * 50)
