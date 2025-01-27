import numpy as np
from src.integration import integrate_newton


s_wave = np.loadtxt("C:/Users/Viktor/GOPH_420/repos/goph420_w2025_lab01_stVP/data/s_wave_data.txt", dtype='float')

x = s_wave[:, 0]
f = s_wave[:, 1]

max_velocity = np.max(np.abs(f))
threshold = 0.005 * max_velocity
T_index = np.where(np.abs(f) > threshold)[0][-1]
T = x[T_index]

alg = "trap"

v_trap = integrate_newton(x, f, alg) / T
print(f"Average squared velocity (v^2_avg): {v_trap:.4f} mm^2/s^2")

alg = "simp"
v_simp = integrate_newton(x, f, alg) / T
print(f"Average squared velocity (v^2_avg): {v_simp:.4f} mm^2/s^2")

