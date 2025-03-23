import numpy as np
import matplotlib.pyplot as plt

# Given constants for 1040 steel
Kic = 54.0  # MPa * sqrt(m)
Y = 1.0     # geometry factor (assumed = 1.0)

# Create an array of flaw sizes from 0.1 m down to 0.001 m on a log scale
a_values = np.logspace(-3, -1, num=50)[::-1]  
# Explanation: 
#   np.logspace(-3, -1, 50) generates 50 points from 1e-3 to 1e-1
#   [::-1] reverses the array so it goes from larger to smaller.
# If you prefer the opposite direction (small to large), remove [::-1].

# Calculate critical stress for each flaw size
# σ_crit = Kic / (Y * sqrt(pi * a))  (here Y=1, so it simplifies)
sigma_crit = Kic / np.sqrt(np.pi * a_values)

# Plot the Failure Design Curve
plt.figure(figsize=(8, 6))
plt.plot(a_values, sigma_crit, 'ro-', markersize=4, label='Failure Curve')

# Label axes
plt.xlabel('Flaw Size, a (m)', fontsize=12)
plt.ylabel('Critical Stress, σ₍crit₎ (MPa)', fontsize=12)
plt.title('Failure Design Plot for 1040 Steel', fontsize=14)

# Use a log scale for flaw size (often done for crack sizes)
plt.xscale('log')

# Optional grid and legend
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()

# Show the plot
plt.show()
