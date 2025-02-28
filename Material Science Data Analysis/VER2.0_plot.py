import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Specimen Measurements in mm
thickness_mm = 3.0        
width_mm = 13.0           
gauge_length_mm = 80.0    

# Convert dimensions to meters for calculations
thickness = thickness_mm / 1000  
width = width_mm / 1000          
gauge_length = gauge_length_mm / 1000  

# Calculate original cross-sectional area (in m^2)
A0 = thickness * width


# Load CSV data (update the path if necessary)
data = pd.read_csv(r'C:\Users\nikit\OneDrive\Docs\GitHub\Learn-Python\Learn-python\Material Science Data Analysis\Specimen_RawData_1_2.csv')
# Clean up column names (remove extra spaces)
data.columns = data.columns.str.strip()
#print("Columns found in CSV:", data.columns)

# ---------------------------
# Determine the correct displacement/extension column by searching for a column containing 'Extension'
disp_col = None
for col in data.columns:
    if "Extension" in col:
        disp_col = col
        break
if disp_col is None:
    raise KeyError("CSV file must contain a column with 'Extension' in its name.")

# Determine the correct force column by searching for a column containing 'Load'
force_col = None
for col in data.columns:
    if "Load" in col:
        force_col = col
        break
if force_col is None:
    raise KeyError("CSV file must contain a column with 'Load' in its name.")

# Convert displacement (extension) to meters
data['Displacement_m'] = data[disp_col] / 1000

# ---------------------------
# Calculate Engineering Stress and Engineering Strain and Engineering UTS
data['Engineering_Stress'] = data[force_col] / A0  # Stress in Pascals (N/m^2)
data['Engineering_Strain'] = data['Displacement_m'] / gauge_length
engineering_UTS_Pa = data['Engineering_Stress'].max()
engineering_UTS_MPa = round((engineering_UTS_Pa / 1e6), 2)
print("Engineering UTS in MPa", engineering_UTS_MPa)



# !!!!!!!!!!!!!!!!!!---------
# Define a more restrictive elastic region
elastic_limit = 0.02  # Use strains below 2%
linear_region = data[data['Engineering_Strain'] < elastic_limit]
slope, intercept = np.polyfit(linear_region['Engineering_Strain'], linear_region['Engineering_Stress'], 1)
E = slope  # in Pa
E_inGpa = E / 1e9
E_inMpa = E / 1e6
print("New Estimated E =", E, "Pa")
print(E_inGpa, "GPa")
print(E_inMpa, "MPa")
# Estimate Young's Modulus (E) from the initial linear region (strain < 0.1)
# linear_region = data[data['Engineering_Strain'] < 0.1]
# slope, intercept = np.polyfit(linear_region['Engineering_Strain'], 
#                               linear_region['Engineering_Stress'], 1)
# E = slope  # in Pa

# Create the 0.2% offset line
offset = 0.002  # 0.2%
strain_vals = data['Engineering_Strain'].values


# CHECK THIS FORMULA
offset_stress = E * (strain_vals - offset)
#offset_stress = np.where(strain_vals >= offset, E * (strain_vals - offset), np.nan)

# Find the yield point by finding where the absolute difference between the actual stress
# and the offset line is minimized.
diff = np.abs(data['Engineering_Stress'] - offset_stress)
yield_index = diff.idxmin()
yield_strain = data.loc[yield_index, 'Engineering_Strain']
yield_stress = data.loc[yield_index, 'Engineering_Stress']

# ---------------------------
# Calculate UTS (Ultimate Tensile Strength) and % Elongation
UTS = data['Engineering_Stress'].max()
percent_elongation = (data['Displacement_m'].iloc[-1] / gauge_length) * 100

# ---------------------------
# Plot 1: Engineering Stress vs. Engineering Strain (Full Range)
plt.figure(figsize=(10, 6))
plt.plot(strain_vals, data['Engineering_Stress'] / 1e6, label='Engineering Stress-Strain')
plt.plot(strain_vals, offset_stress / 1e6, '--', label='0.2% Offset Line')
plt.plot(yield_strain, yield_stress / 1e6, 'ro', 
         label=f'Yield Point\n({yield_stress/1e6:.2f} MPa)')
plt.xlabel('Engineering Strain')
plt.ylabel('Engineering Stress (MPa)')
plt.title('Engineering Stress vs. Engineering Strain (Full Range)')
plt.legend()
plt.grid(True)
plt.annotate(f'UTS: {UTS/1e6:.2f} MPa', 
             xy=(data['Engineering_Strain'][np.argmax(data['Engineering_Stress'])],
                 UTS/1e6),
             xytext=(0.05, UTS/1e6+10),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(f'% Elongation: {percent_elongation:.1f}%', 
             xy=(strain_vals[-1], data['Engineering_Stress'].iloc[-1]/1e6),
             xytext=(strain_vals[-1]-0.1, data['Engineering_Stress'].iloc[-1]/1e6+10),
             arrowprops=dict(facecolor='black', shrink=0.05))   
plt.tight_layout()
plt.show()

# ---------------------------
# Plot 2: Engineering Stress vs. Engineering Strain (Low Strain Region)
plt.figure(figsize=(10, 6))
zoom_mask = data['Engineering_Strain'] < 0.05
plt.plot(data.loc[zoom_mask, 'Engineering_Strain'], 
         data.loc[zoom_mask, 'Engineering_Stress'] / 1e6, label='Engineering Stress-Strain')
plt.plot(data.loc[zoom_mask, 'Engineering_Strain'], 
         (E * (data.loc[zoom_mask, 'Engineering_Strain'] - offset)) / 1e6, '--', 
         label='0.2% Offset Line')
plt.plot(yield_strain, yield_stress / 1e6, 'ro', 
         label=f'Yield Point\n({yield_stress/1e6:.2f} MPa)')
plt.xlabel('Engineering Strain')
plt.ylabel('Engineering Stress (MPa)')
plt.title('Engineering Stress vs. Engineering Strain (Low Strain Region)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------
# Calculate True Stress and True Strain
data['True_Strain'] = np.log(1 + data['Engineering_Strain'])
data['True_Stress'] = data['Engineering_Stress'] * (1 + data['Engineering_Strain'])

# ---------------------------
# Fit the Strain Hardening Curve: σ = K * (ε)^n
# Use data points in the plastic region (True_Strain > ln(1 + yield_strain))
plastic_mask = data['True_Strain'] > np.log(1 + yield_strain)
def strain_hardening(epsilon, K, n):
    return K * (epsilon ** n)

# Perform curve fitting
popt, pcov = curve_fit(strain_hardening, 
                       data.loc[plastic_mask, 'True_Strain'], 
                       data.loc[plastic_mask, 'True_Stress'], 
                       p0=[900e6, 0.25])
K_fitted, n_fitted = popt

# ---------------------------
# Plot 3: True Stress vs. True Strain with Fitted Strain Hardening Curve
plt.figure(figsize=(10, 6))
plt.plot(data['True_Strain'], data['True_Stress'] / 1e6, label='True Stress-Strain Data')
strain_fit = np.linspace(data['True_Strain'].min(), data['True_Strain'].max(), 200)
plt.plot(strain_fit, strain_hardening(strain_fit, K_fitted, n_fitted) / 1e6, '--', 
         label=f'Fitted Curve\nK = {K_fitted/1e6:.1f} MPa, n = {n_fitted:.2f}')
plt.xlabel('True Strain')
plt.ylabel('True Stress (MPa)')
plt.title('True Stress vs. True Strain with Strain Hardening Curve Fit')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------
# Specimen Properties Table (using your provided measurements)
specimen_properties = {
    'Parameter': ['Initial Thickness (mm)', 'Initial Width (mm)', 'Initial Gauge Length (mm)',
                  'Final Thickness (mm)', 'Final Width (mm)', 'Final Gauge Length (mm)',
                  'Initial Hardness', 'Final Hardness'],
    'Value': [thickness_mm, width_mm, gauge_length_mm,
              np.mean([2.85, 1.8, 2.85]),   # Final thickness average from your data
              np.mean([12.6, 9.5, 12.6]),    # Final width average from your data
              110,                         # Final gauge length as given
              51.03333333,                 # Initial Hardness average
              66.26666667]                 # Final Hardness average
}

specimen_df = pd.DataFrame(specimen_properties)
print("\nSpecimen Properties Table:")
print(specimen_df)

#-----------------------AFTER I WATCHED  THE VIDEO-------------------
#calc Yield Stress
offset = 0.002
bOffset = -E * offset
stressOffset = E * data['Engineering_Strain'] + bOffset
offsetDelta = np.abs(data['Engineering_Stress'] - stressOffset)
yieldIndex = offsetDelta.idxmin()
yieldStress = data.loc[yieldIndex, 'Engineering_Stress']
yieldStrain = data.loc[yieldIndex, 'Engineering_Strain']
#print("\nYield Stress:", yieldStress, "Pa")
yieldStressMPa = yieldStress / 1e6
#print(yieldStressMPa, "MPa")
#print("Yield Strain:", yieldStrain)

#True Stress and True Strain
trueStress = data['Engineering_Stress'] * (1 + data['Engineering_Strain'])
#make trueStress to UTS
trueUTS = trueStress.max()
trueUTSMPa = trueUTS / 1e6
print("True UTS:", trueUTSMPa, "MPa")
percentElongation = (data['Displacement_m'].iloc[-1] / gauge_length) * 100
rounded_percentElongation = round(percent_elongation, 0)
print("Percent Elongation:", rounded_percentElongation, "%")

trueStrain = np.log(1 + data['Engineering_Strain'])
#make trueStrain to UTS
UTSIndex = trueStress.idxmax()
UTSStrain = trueStrain[UTSIndex]

#plot Engineering vs True Stress and Strain
plt.figure(figsize=(10, 6))
plt.plot(data['Engineering_Strain'], data['Engineering_Stress'] / 1e6, label='Engineering Stress-Strain')
plt.plot(trueStrain, trueStress / 1e6, label='True Stress-Strain')
plt.plot(yieldStrain, yieldStress / 1e6, 'ro', label=f'Yield Point\n({yieldStressMPa:.2f} MPa)')
plt.plot(UTSStrain, trueUTS / 1e6, 'go', label=f'True UTS\n({trueUTSMPa:.2f} MPa)')
plt.xlabel('Strain')
plt.ylabel('Stress (MPa)')
plt.title('Engineering vs True Stress and Strain')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
