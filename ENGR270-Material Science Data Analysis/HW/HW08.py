import numpy as np
import matplotlib.pyplot as plt

# Given constants
Kic = 54.0  # MPa * sqrt(m)
Y = 1.0     # geometry factor (assumed)

# Generate a range of flaw sizes (in meters)
# For example, from 1e-4 m up to 0.1 m on a logarithmic scale
a_values = np.logspace(-4, -1, num=50)  # 50 points between 1e-4 and 1e-1

# Calculate critical stress for each flaw size
# sigma_crit = Kic / sqrt(pi * a)
sigma_crit = Kic / np.sqrt(np.pi * a_values)  # MPa

# Plot the Failure Design Curve
plt.figure(figsize=(8, 6))
plt.plot(a_values, sigma_crit, 'b-o', markersize=4, label='Failure Curve')

# Label axes
plt.xlabel('Flaw Size a (m)', fontsize=12)
plt.ylabel('Critical Stress σ₍crit₎ (MPa)', fontsize=12)
plt.title('Failure Design Plot for 1040 Steel', fontsize=14)

# Use a log scale for flaw size (often done for crack sizes)
plt.xscale('log')

# Optional grid and legend
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()

# Show the plot
plt.show()
