import numpy as np
import matplotlib.pyplot as plt

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Fit a polynomial of degree 2
coefficients = np.polyfit(x, y, 2)
print(coefficients)

# Generate points for the fitted polynomial
x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = np.polyval(coefficients, x_fit)

# Plot the original data and the fitted polynomial
plt.scatter(x, y, label='Original data')
plt.plot(x_fit, y_fit, label='Fitted polynomial')
plt.legend()
plt.show()