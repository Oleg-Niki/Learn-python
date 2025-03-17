import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data (update the file path as needed)
data = pd.read_csv(r"C:\Users\nikit\GitHub\Learn-python-3\ENGR270-Material Science Data Analysis\Lab4\Specimen_RawData_1.csv" , header=0)
print(data.columns)
data.columns = data.columns.str.strip()
print(data.columns)

data.rename(columns={'Tensile strain (Strain 1) (mm/mm)': 'Strain'}, inplace=True)
print("Min strain:", data['Strain'].min())
print("Max strain:", data['Strain'].max())


# Assuming the CSV has columns 'Force' and 'Displacement'
# Also assuming you have the cross-sectional area (A) and original length (L) defined:
A = 1.0e-4  # example: in square meters
L = 0.05    # example: in meters

# Calculate stress (Pa) and strain (dimensionless)
data['Stress'] = data['Load (N)'] / A
data['Strain'] = data['Extension (mm)'] / L

# Plot the stress-strain curve to visually identify the linear region
plt.figure(figsize=(8,6))
plt.plot(data['Strain'], data['Stress'], label='Stress-Strain Curve')
plt.xlabel('Strain (dimensionless)')
plt.ylabel('Stress (Pa)')
plt.title('Stress-Strain Curve')
plt.legend()
plt.show()

# For demonstration, suppose the elastic region is between strain = 0 and strain = 0.005
elastic_region = data[(data['Strain'] >= 0) & (data['Strain'] <= 0.005)]

# Perform linear regression on the elastic region
slope, intercept, r_value, p_value, std_err = linregress(elastic_region['Strain'], elastic_region['Stress'])
E_Pa = slope  # modulus in Pascals
E_GPa = E_Pa / 1e9  # convert to GPa

print(f"Modulus of Elasticity: {E_GPa:.3f} GPa")
