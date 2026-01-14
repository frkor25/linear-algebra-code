import numpy as np

# ========== DEFINE YOUR VECTOR AND TRANSFORMATION HERE ==========

# Choose your vector (2D or 3D)
vector = np.array([3, 1])           # 2D vector example
# vector = np.array([1, 2, 3])      # 3D vector example (uncomment to use)

# Choose your transformation type (uncomment ONE):

# 2D Transformations:
transformation_type = "rotation_2d"
angle = 90                           # Rotation angle in degrees

# transformation_type = "scaling_2d"
# sx, sy = 2, 0.5                    # Scaling factors for x and y

# transformation_type = "reflection_x"

# transformation_type = "reflection_y"

# transformation_type = "shearing_horizontal"
# k = 1.5                            # Shearing factor

# transformation_type = "shearing_vertical"
# k = 1.5                            # Shearing factor

# 3D Transformations:
# transformation_type = "rotation_3d_x"
# angle = 45                         # Rotation angle in degrees

# transformation_type = "rotation_3d_y"
# angle = 45                         # Rotation angle in degrees

# transformation_type = "rotation_3d_z"
# angle = 45                         # Rotation angle in degrees

# transformation_type = "scaling_3d"
# sx, sy, sz = 2, 2, 0.5            # Scaling factors for x, y, and z

# =================================================================


def rotation_matrix_2d(angle_degrees):
    theta = np.radians(angle_degrees)
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

def rotation_matrix_3d_x(angle_degrees):
    theta = np.radians(angle_degrees)
    return np.array([[1, 0, 0],
                     [0, np.cos(theta), -np.sin(theta)],
                     [0, np.sin(theta), np.cos(theta)]])

def rotation_matrix_3d_y(angle_degrees):
    theta = np.radians(angle_degrees)
    return np.array([[np.cos(theta), 0, np.sin(theta)],
                     [0, 1, 0],
                     [-np.sin(theta), 0, np.cos(theta)]])

def rotation_matrix_3d_z(angle_degrees):
    theta = np.radians(angle_degrees)
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])

def scaling_matrix_2d(sx, sy):
    return np.array([[sx, 0],
                     [0, sy]])

def scaling_matrix_3d(sx, sy, sz):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, sz]])

def reflection_matrix_2d_x():
    return np.array([[1, 0],
                     [0, -1]])

def reflection_matrix_2d_y():
    return np.array([[-1, 0],
                     [0, 1]])

def shearing_matrix_2d_x(k):
    return np.array([[1, k],
                     [0, 1]])

def shearing_matrix_2d_y(k):
    return np.array([[1, 0],
                     [k, 1]])

def get_vector_magnitude(vector):
    return np.linalg.norm(vector)

def get_vector_angle_2d(vector):
    return np.degrees(np.arctan2(vector[1], vector[0]))


# Apply the transformation
if transformation_type == "rotation_2d":
    matrix = rotation_matrix_2d(angle)
    name = f"Rotation by {angle}°"
elif transformation_type == "rotation_3d_x":
    matrix = rotation_matrix_3d_x(angle)
    name = f"Rotation around x-axis by {angle}°"
elif transformation_type == "rotation_3d_y":
    matrix = rotation_matrix_3d_y(angle)
    name = f"Rotation around y-axis by {angle}°"
elif transformation_type == "rotation_3d_z":
    matrix = rotation_matrix_3d_z(angle)
    name = f"Rotation around z-axis by {angle}°"
elif transformation_type == "scaling_2d":
    matrix = scaling_matrix_2d(sx, sy)
    name = f"Scaling (sx={sx}, sy={sy})"
elif transformation_type == "scaling_3d":
    matrix = scaling_matrix_3d(sx, sy, sz)
    name = f"Scaling (sx={sx}, sy={sy}, sz={sz})"
elif transformation_type == "reflection_x":
    matrix = reflection_matrix_2d_x()
    name = "Reflection across x-axis"
elif transformation_type == "reflection_y":
    matrix = reflection_matrix_2d_y()
    name = "Reflection across y-axis"
elif transformation_type == "shearing_horizontal":
    matrix = shearing_matrix_2d_x(k)
    name = f"Horizontal shearing (k={k})"
elif transformation_type == "shearing_vertical":
    matrix = shearing_matrix_2d_y(k)
    name = f"Vertical shearing (k={k})"
else:
    print("Invalid transformation type!")
    exit()

# Perform transformation
transformed_vector = matrix @ vector

# Print results
print("=" * 70)
print(f"TRANSFORMATION: {name}")
print("=" * 70)
print("Original vector:")
print(vector)
print(f"Magnitude: {get_vector_magnitude(vector):.4f}")

if len(vector) == 2:
    print(f"Angle: {get_vector_angle_2d(vector):.2f}°")

print("-" * 70)
print("Transformation matrix:")
print(matrix)
print("-" * 70)
print("Transformed vector:")
print(transformed_vector)
print(f"Magnitude: {get_vector_magnitude(transformed_vector):.4f}")

if len(transformed_vector) == 2:
    print(f"Angle: {get_vector_angle_2d(transformed_vector):.2f}°")

# Analysis
print("-" * 70)
print("ANALYSIS:")
original_mag = get_vector_magnitude(vector)
transformed_mag = get_vector_magnitude(transformed_vector)
mag_change = transformed_mag / original_mag if original_mag != 0 else 0
print(f"Magnitude change: {mag_change:.4f}x")

if len(vector) == 2:
    original_angle = get_vector_angle_2d(vector)
    transformed_angle = get_vector_angle_2d(transformed_vector)
    angle_change = transformed_angle - original_angle
    print(f"Angle change: {angle_change:.2f}°")

det = np.linalg.det(matrix)
print(f"Determinant: {det:.4f}")

if abs(abs(det) - 1) < 1e-10:
    if len(vector) == 2:
        print("→ Preserves area (orthogonal transformation)")
    else:
        print("→ Preserves volume (orthogonal transformation)")
elif det > 0:
    print("→ Preserves orientation")
elif det < 0:
    print("→ Reverses orientation")

print("=" * 70)
