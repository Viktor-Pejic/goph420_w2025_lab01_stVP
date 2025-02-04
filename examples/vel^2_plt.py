import numpy as np
import matplotlib.pyplot as plt

s_wave = np.loadtxt("C:/Users/Viktor/GOPH_420/repos/goph420_w2025_lab01_stVP/data/s_wave_data.txt", dtype='float')

time = s_wave[:, 0]
vel = s_wave[:, 1]
vel_2 = vel**2

plt.plot(time,vel_2)
plt.title('Time vs Velocity Plot')
plt.xlabel('Time (s)')
plt.ylabel('Velocity ^ 2 (mm^2/s^2)')
plt.grid(True)
plt.savefig("C:/Users/Viktor/GOPH_420/repos/goph420_w2025_lab01_stVP/figures/Vel^2_data.png")
