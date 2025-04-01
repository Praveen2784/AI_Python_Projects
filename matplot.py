import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec  # For custom layout

x = np.array([2020, 2021, 2022, 2023, 2024, 2025])
y = np.array([7, 8, 9, 10, 12, 14])
y_fahrenheit = (y * 9 / 5) + 32

fig = plt.figure(figsize=(8, 8))
gs = gridspec.GridSpec(3, 1, height_ratios=[1, 1, 1])  # VStack (3 rows, 1 column)

# First subplot (Top) - Fahrenheit
ax1 = plt.subplot(gs[0, 0])
ax1.plot(x, y_fahrenheit, 'bo-', label='Fahrenheit')
ax1.set_xlabel('Years')
ax1.set_ylabel('Temperature in Fahrenheit')
ax1.legend()

# Second subplot (Middle) - Celsius
ax2 = plt.subplot(gs[1, 0])
ax2.plot(x, y, 'r*-', label='Celsius')
ax2.set_xlabel('Years')
ax2.set_ylabel('Temperature in Celsius')
ax2.legend()

# Third subplot (Bottom) - Another Fahrenheit example
ax3 = plt.subplot(gs[2, 0])
ax3.plot(x, y_fahrenheit, 'bo-', label='Fahrenheit')
ax3.set_xlabel('Years')
ax3.set_ylabel('Temperature in Rain')
ax3.legend()

fig.suptitle('Temperature in Helsinki in last 6 years', fontsize=14)

plt.tight_layout()
plt.show()
