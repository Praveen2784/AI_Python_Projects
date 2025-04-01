import numpy as np

# Define the original array
Xstage = np.array([1, 2, 3, 4, 5])

# Create a copy of Xstage
vstage = Xstage.copy()

# Modify vstage to check if it's independent of Xstage
vstage[0] = 99

# Print both arrays
print("Xstage:", Xstage)  # Output: [1, 2, 3, 4, 5]
print("vstage:", vstage)  # Output: [99, 2, 3, 4, 5]

# Define the original 2D array
Xstage = np.array([[1, 2, 3], [4, 5, 6]])

# Create a copy of Xstage
vstage = Xstage.copy()

# Iterate through all elements using 'ij' (row, column) indexing
print("Elements in Xstage:")
for i, j in np.ndindex(Xstage.shape):
    print(f"Xstage[{i}, {j}] = {Xstage[i, j]}")

print("\nElements in vstage (copy of Xstage):")
for i, j in np.ndindex(vstage.shape):
    print(f"vstage[{i}, {j}] = {vstage[i, j]}")



# Declare a 2D array (Xstage)
Xstage = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Create an independent copy (vstage)
vstage = Xstage.copy()

# Read all elements using (i, j) indexing
print("Reading elements from Xstage:")
for i in range(Xstage.shape[0]):  # Iterate over rows
    for j in range(Xstage.shape[1]):  # Iterate over columns
        print(f"Xstage[{i}][{j}] = {Xstage[i, j]}")

print("\nReading elements from vstage (copy of Xstage):")
for i in range(vstage.shape[0]):  # Iterate over rows
    for j in range(vstage.shape[1]):  # Iterate over columns
        print(f"vstage[{i}][{j}] = {vstage[i, j]}")