import numpy as np

# Define the range and amount
a = 1
b = 16
amount = 50

# Generate random integers between [a, b]
nopat = np.random.randint(a, b+1, amount)

# Print the result
print(nopat)
