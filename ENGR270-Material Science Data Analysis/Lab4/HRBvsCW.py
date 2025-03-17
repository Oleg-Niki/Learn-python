import numpy as np
import matplotlib.pyplot as plt

# --- Measured Data for Hardness (HRB) from 3 points per cycle ---
hardness_data = {
    0: [80, 79.8, 79.8],
    1: [79.8, 81.8, 80],
    2: [81.5, 84, 82.9],
    3: [80.1, 82.3, 83.4],
    4: [85.4, 83.5, 82.6],
    5: [86.7, 90.5, 88.9]
}

# --- Measured Dimensions (Width and Thickness in mm) from 3 points per cycle ---
width_data = {
    0: [13.56, 13.5, 13.5],
    1: [13.42, 13.42, 13.41],
    2: [13.31, 13.3, 13.3],
    3: [13.3, 13.2, 13.33],
    4: [13.17, 13.11, 13.15],
    5: [12.8, 12.14, 12.37]
}
thickness_data = {
    0: [3.2, 3.18, 3.18],
    1: [3.17, 3.16, 3.17],
    2: [3.16, 3.14, 3.14],
    3: [3.16, 3.1, 3.16],
    4: [3.16, 3.13, 3.11],
    5: [3, 2.77, 2.96]
}

cycles = [0, 1, 2, 3, 4, 5]

# --- Compute Means and Standard Deviations ---
mean_hardness = []
std_hardness = []
mean_area = []
std_area = []
percent_cw = []
err_percent_cw = []

for cycle in cycles:
    # Hardness statistics:
    h = np.array(hardness_data[cycle])
    mean_h = np.mean(h)
    std_h = np.std(h, ddof=1)  # sample standard deviation
    mean_hardness.append(mean_h)
    std_hardness.append(std_h)
    
    # Compute cross-sectional areas from width and thickness measurements:
    w = np.array(width_data[cycle])
    t = np.array(thickness_data[cycle])
    areas = w * t  # element-wise multiplication
    mean_a = np.mean(areas)
    std_a = np.std(areas, ddof=1)
    mean_area.append(mean_a)
    std_area.append(std_a)

# Use Cycle 0's mean area as the reference area A0.
A0 = mean_area[0]

for cycle in cycles:
    A = mean_area[cycle]
    # %CW = 100 * (A0 - A) / A0
    cw = 100 * (A0 - A) / A0
    percent_cw.append(cw)
    # Propagate error: sigma(%CW) ≈ (100/A0)*sigma_A
    err_cw = 100 / A0 * std_area[cycle]
    err_percent_cw.append(err_cw)

# --- Plot 1: Hardness vs. %CW with Error Bars and Connected Line ---
plt.figure()
plt.errorbar(percent_cw, mean_hardness, yerr=std_hardness, xerr=err_percent_cw,
             fmt='-o', capsize=5, ecolor='black')
plt.xlabel("% Cold Work")
plt.ylabel("Hardness (HRB)")
plt.title("Plot 1: Hardness vs. %CW")
plt.grid(True)
plt.show()
