import numpy as np

# Define the longitude and latitude coordinates of the four points forming the square shape
ilon = np.array([0.0, 0.0, np.pi/2, np.pi/2])  # Longitude coordinates in radians
ilat = np.array([0.0, np.pi/2, np.pi/2, 0.0])  # Latitude coordinates in radians

# Define the longitude and latitude coordinates of the other four points forming the square shape
olon = np.array([np.pi, np.pi, 3*np.pi/2, 3*np.pi/2])  # Longitude coordinates in radians
olat = np.array([0.0, np.pi/2, np.pi/2, 0.0])  # Latitude coordinates in radians

# Convert the coordinates to Cartesian coordinates using the spherical coordinate system
x_i = np.cos(ilon) * np.sin(ilat)
y_i = np.sin(ilon) * np.sin(ilat)
z_i = np.cos(ilat)

x_o = np.cos(olon) * np.sin(olat)
y_o = np.sin(olon) * np.sin(olat)
z_o = np.cos(olat)

# Combine the Cartesian coordinates for the two sets of points
x = np.concatenate((x_i, x_o))
y = np.concatenate((y_i, y_o))
z = np.concatenate((z_i, z_o))

# Convert the Cartesian coordinates to spherical coordinates with origin at the center of the Earth
r = np.sqrt(x**2 + y**2 + z**2)
theta = np.arccos(z/r)
phi = np.arctan2(y, x)

# Calculate the dot product of the unit vectors corresponding to each point
dot = np.dot(np.transpose([x_i, y_i, z_i]), [x_o, y_o, z_o])

# Find the overlapping area in steradians
overlapping_area = 2 * np.arccos(dot.min())

# Find the non-overlapping area in steradians
non_overlapping_area = 2 * np.pi - overlapping_area

# Find the ratio of the non-overlapping area to the overlapping area
ratio = non_overlapping_area / overlapping_area

print(f"Overlapping area: {overlapping_area:.4f} steradians")
print(f"Non-overlapping area: {non_overlapping_area:.4f} steradians")
print(f"Ratio of non-overlapping area to overlapping area: {ratio:.4f}")
