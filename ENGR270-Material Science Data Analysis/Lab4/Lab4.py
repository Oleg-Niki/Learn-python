import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

###############################################################################
# 1) Read the Cycle-Based Data for Plot 1, 4, 5, and 6
###############################################################################
df_cycle = pd.read_csv(
    r"C:\Users\nikit\GitHub\Learn-python-3\ENGR270-Material Science Data Analysis\Lab4\E270Lab04StrainHardeningLabTemplate(OlegForPython).csv"
)

# Check and generate approximate columns if missing.
if "YieldStrength_MPa" not in df_cycle.columns:
    print("Column 'YieldStrength_MPa' not found in cycle-based data; generating approximate yield strength from Hardness_HRB.")
    # Example empirical correlation: yield strength ≈ 0.9 * 3.45 * Hardness (HRB)
    df_cycle["YieldStrength_MPa"] = 0.9 * 3.45 * df_cycle["Hardness_HRB"]

if "Ductility_pct" not in df_cycle.columns:
    print("Column 'Ductility_pct' not found in cycle-based data; assigning NaN values.")
    df_cycle["Ductility_pct"] = np.nan

if "E_GPa" not in df_cycle.columns:
    print("Column 'E_GPa' not found in cycle-based data; assigning default value of 200 GPa.")
    df_cycle["E_GPa"] = 200

###############################################################################
# 2) Plot 1: Hardness (HRB) vs. %CW
###############################################################################
plt.figure()
plt.plot(df_cycle["PercentCW"], df_cycle["Hardness_HRB"], marker='o')
plt.xlabel("Percent Cold Work (%CW)")
plt.ylabel("Hardness (HRB)")
plt.title("Plot 1: Hardness vs. %CW")
plt.grid(True)
plt.show()

###############################################################################
# 3) Prepare for Reading the Raw Instron Data for Plot 2 and Plot 3
###############################################################################
filenames = [
    r"C:\Users\nikit\GitHub\Learn-python-3\ENGR270-Material Science Data Analysis\Lab4\Specimen_RawData_1.csv",
    r"C:\Users\nikit\GitHub\Learn-python-3\ENGR270-Material Science Data Analysis\Lab4\Specimen_RawData_1 (1).csv",
    r"C:\Users\nikit\GitHub\Learn-python-3\ENGR270-Material Science Data Analysis\Lab4\Specimen_RawData_1 (2).csv",
    r"C:\Users\nikit\GitHub\Learn-python-3\ENGR270-Material Science Data Analysis\Lab4\Specimen_RawData_1 (3).csv",
    r"C:\Users\nikit\GitHub\Learn-python-3\ENGR270-Material Science Data Analysis\Lab4\Specimen_RawData_1 (4).csv"
]

# Assume that the "Cycle 0" row in df_cycle contains the initial dimensions:
width0 = df_cycle.loc[df_cycle["Cycle"] == 0, "Width_mm"].values[0]
thickness0 = df_cycle.loc[df_cycle["Cycle"] == 0, "Thickness_mm"].values[0]
gaugeLen0 = df_cycle.loc[df_cycle["Cycle"] == 0, "GaugeLength_mm"].values[0]

A0 = width0 * thickness0  # Initial cross-sectional area (mm^2)
L0 = gaugeLen0            # Initial gauge length (mm)

# For Plot 3, prepare updated cross-sectional area and gauge length for each cycle:
Ai_dict = {}
Li_dict = {}
for i, row in df_cycle.iterrows():
    cycle_num = row["Cycle"]
    w = row["Width_mm"]
    t = row["Thickness_mm"]
    l = row["GaugeLength_mm"]
    Ai_dict[cycle_num] = w * t   # Updated area for that cycle
    Li_dict[cycle_num] = l       # Updated gauge length for that cycle

###############################################################################
# 4) PLOT 2: Combined Engineering Stress-Strain (all cycles) using Original A0, L0
###############################################################################
plt.figure()
strain_offset = 0.0

for cycle_index, fname in enumerate(filenames):
    # Read each raw CSV file (assume the first row is the header row)
    df_raw = pd.read_csv(fname, header=0)
    
    # Debug: print out the columns for verification
    print(f"\nFile: {fname}")
    print("Columns found:", df_raw.columns)
    
    # Remove any extra spaces from column names
    df_raw.columns = df_raw.columns.str.strip()
    
    # Rename columns if necessary
    if "Load (N)" in df_raw.columns:
        df_raw.rename(columns={"Load (N)": "Load"}, inplace=True)
    if "Extension (mm)" in df_raw.columns:
        df_raw.rename(columns={"Extension (mm)": "Extension"}, inplace=True)
    
    load_col = "Load"
    extension_col = "Extension"
    
    # Convert columns to numeric
    df_raw[load_col] = pd.to_numeric(df_raw[load_col], errors="coerce")
    df_raw[extension_col] = pd.to_numeric(df_raw[extension_col], errors="coerce")
    
    # Compute engineering stress and strain (using original A0 and L0)
    df_raw["Eng_Stress"] = df_raw[load_col] / A0
    df_raw["Eng_Strain"] = df_raw[extension_col] / L0
    
    # ----- Toe Compensation -----
    # Subtract the minimum strain value (toe region) so that the cycle starts at zero strain.
    toe_comp = df_raw["Eng_Strain"].min()
    df_raw["Eng_Strain"] = df_raw["Eng_Strain"] - toe_comp
    # --------------------------------
    
    # Apply the accumulated strain offset (permanent plastic strain from previous cycles)
    df_raw["Eng_Strain_Shifted"] = df_raw["Eng_Strain"] + strain_offset
    
    # Update offset for next cycle (use final shifted strain value)
    new_offset = df_raw["Eng_Strain_Shifted"].iloc[-1]
    
    plt.plot(df_raw["Eng_Strain_Shifted"], df_raw["Eng_Stress"], label=f"Cycle {cycle_index+1}")
    strain_offset = new_offset

plt.xlabel("Engineering Strain (mm/mm)")
plt.ylabel("Engineering Stress (MPa)")
plt.title("Plot 2: Combined Eng. Stress-Strain (Original A0, L0)")
plt.legend()
plt.grid(True)
plt.show()

###############################################################################
# 5) PLOT 3: Engineering Stress-Strain for Each Cycle using UPDATED Ai, Li
#     with Elastic Region (Young’s Modulus) and 0.2% Offset Lines
###############################################################################
plt.figure()

for cycle_index, fname in enumerate(filenames):
    df_raw = pd.read_csv(fname, header=0)
    
    # Strip extra spaces and rename columns if needed.
    df_raw.columns = df_raw.columns.str.strip()
    if "Load (N)" in df_raw.columns:
        df_raw.rename(columns={"Load (N)": "Load"}, inplace=True)
    if "Extension (mm)" in df_raw.columns:
        df_raw.rename(columns={"Extension (mm)": "Extension"}, inplace=True)
    
    load_col = "Load"
    extension_col = "Extension"
    
    # Convert columns to numeric.
    df_raw[load_col] = pd.to_numeric(df_raw[load_col], errors="coerce")
    df_raw[extension_col] = pd.to_numeric(df_raw[extension_col], errors="coerce")
    
    # Determine cycle number (0-based indexing)
    cycle_number = cycle_index
    Ai = Ai_dict.get(cycle_number, A0)
    Li = Li_dict.get(cycle_number, L0)
    
    # Compute engineering stress and strain using updated dimensions.
    df_raw["Eng_Stress"] = df_raw[load_col] / Ai
    df_raw["Eng_Strain"] = df_raw[extension_col] / Li
    
    # ----- Toe Compensation -----
    # Subtract the minimum measured strain to remove the toe region.
    toe_comp = df_raw["Eng_Strain"].min()
    df_raw["Eng_Strain"] = df_raw["Eng_Strain"] - toe_comp
    # --------------------------------
    
    # Plot the experimental stress-strain curve.
    plt.plot(df_raw["Eng_Strain"], df_raw["Eng_Stress"], label=f"Cycle {cycle_number}")
    
    # --- Estimate Young's Modulus from the initial elastic region ---
    # Define threshold for elastic region (e.g., strain < 0.005).
    mask = df_raw["Eng_Strain"] < 0.005
    if mask.sum() > 1:
        # Fit a line: stress = E * strain + intercept
        p = np.polyfit(df_raw["Eng_Strain"][mask], df_raw["Eng_Stress"][mask], 1)
        E_est = p[0]  # estimated Young's modulus
        
        # Create a strain range for plotting the elastic line.
        strain_line = np.linspace(0, 0.005, 50)
        stress_line = E_est * strain_line  # elastic line through origin
        
        # Plot the elastic (Young’s Modulus) line in red (solid)
        plt.plot(strain_line, stress_line, 'r-', linewidth=2, label=f"Cycle {cycle_number} E")
        
        # --- Plot the 0.2% Offset Line ---
        # Shift the elastic line by 0.002 (0.2% strain)
        stress_offset = E_est * (strain_line - 0.002)
        plt.plot(strain_line, stress_offset, 'r--', linewidth=2, label=f"Cycle {cycle_number} 0.2% Offset")
        # The intersection of this offset line with your experimental curve is taken as the yield strength.
    
plt.xlabel("Engineering Strain (mm/mm)")
plt.ylabel("Engineering Stress (MPa)")
plt.title("Plot 3: Eng. Stress-Strain (Updated Ai, Li per Cycle)")
plt.legend()
plt.grid(True)
plt.show()


# ###############################################################################
# # 5) PLOT 3: Engineering Stress-Strain for Each Cycle using UPDATED Ai, Li
# ###############################################################################
# plt.figure()

# for cycle_index, fname in enumerate(filenames):
#     df_raw = pd.read_csv(fname, header=0)
    
#     # Strip spaces and rename columns if needed.
#     df_raw.columns = df_raw.columns.str.strip()
#     if "Load (N)" in df_raw.columns:
#         df_raw.rename(columns={"Load (N)": "Load"}, inplace=True)
#     if "Extension (mm)" in df_raw.columns:
#         df_raw.rename(columns={"Extension (mm)": "Extension"}, inplace=True)
    
#     load_col = "Load"
#     extension_col = "Extension"
    
#     df_raw[load_col] = pd.to_numeric(df_raw[load_col], errors="coerce")
#     df_raw[extension_col] = pd.to_numeric(df_raw[extension_col], errors="coerce")
    
#     # Determine cycle number (0-based)
#     cycle_number = cycle_index
#     Ai = Ai_dict.get(cycle_number, A0)
#     Li = Li_dict.get(cycle_number, L0)
    
#     # Compute engineering stress and strain using updated dimensions.
#     df_raw["Eng_Stress"] = df_raw[load_col] / Ai
#     df_raw["Eng_Strain"] = df_raw[extension_col] / Li
    
#     # ----- Toe Compensation -----
#     toe_comp = df_raw["Eng_Strain"].min()
#     df_raw["Eng_Strain"] = df_raw["Eng_Strain"] - toe_comp
#     # --------------------------------
    
#     plt.plot(df_raw["Eng_Strain"], df_raw["Eng_Stress"], label=f"Cycle {cycle_number}")

# plt.xlabel("Engineering Strain (mm/mm)")
# plt.ylabel("Engineering Stress (MPa)")
# plt.title("Plot 3: Eng. Stress-Strain (Updated Ai, Li per Cycle)")
# plt.legend()
# plt.grid(True)
# plt.show()

###############################################################################
# 6) PLOT 4: Yield Strength & Ductility vs. Hardness
###############################################################################
plt.figure()
ax1 = plt.gca()
ax2 = ax1.twinx()

x_data = df_cycle["Hardness_HRB"]
y1_data = df_cycle["YieldStrength_MPa"]
y2_data = df_cycle["Ductility_pct"]

ax1.plot(x_data, y1_data, marker='o')
ax1.set_xlabel("Hardness (HRB)")
ax1.set_ylabel("Yield Strength (MPa)")

ax2.plot(x_data, y2_data, marker='s', linestyle='--')
ax2.set_ylabel("Ductility (%)")

plt.title("Plot 4: Yield Strength & Ductility vs. Hardness")
ax1.grid(True)
plt.show()

###############################################################################
# 7) PLOT 5: Yield Strength & Ductility vs. %CW
###############################################################################
plt.figure()
ax1 = plt.gca()
ax2 = ax1.twinx()

x_data = df_cycle["PercentCW"]
y1_data = df_cycle["YieldStrength_MPa"]
y2_data = df_cycle["Ductility_pct"]

ax1.plot(x_data, y1_data, marker='o')
ax1.set_xlabel("% Cold Work")
ax1.set_ylabel("Yield Strength (MPa)")

ax2.plot(x_data, y2_data, marker='s', linestyle='--')
ax2.set_ylabel("Ductility (%)")

plt.title("Plot 5: Yield Strength & Ductility vs. %CW")
ax1.grid(True)
plt.show()

###############################################################################
# 8) PLOT 6: Young’s Modulus vs. %CW
###############################################################################
plt.figure()
plt.plot(df_cycle["PercentCW"], df_cycle["E_GPa"], marker='o')
plt.xlabel("% Cold Work")
plt.ylabel("Young’s Modulus (GPa)")
plt.title("Plot 6: Young’s Modulus vs. %CW")
plt.grid(True)
plt.show()
