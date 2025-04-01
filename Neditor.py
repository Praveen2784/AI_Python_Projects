import numpy as np
import matplotlib.pyplot as plt

# Define arrays
x = np.array([2020, 2021, 2022, 2023, 2024, 2025])
y = np.array([100, 200, 400, 600, 800, 1000])

# Plot bar chart
plt.bar(x, y, color="green")
plt.title("Title")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()

# Traverse the arrays using np.nditer()
print("Years:")
for year in np.nditer(x):
    print(year, end=" ")

print("\nSales:")
for sales in np.nditer(y):
    print(sales, end=" ")