import numpy as np
import matplotlib.pyplot as plt

s_wave = np.loadtxt("C:/Users/Viktor/GOPH_420/repos/goph420_w2025_lab01_stVP/data/s_wave_data.txt", dtype='float')

time = s_wave[:, 0]
vel = s_wave[:, 1]


plt.plot(time,vel)
plt.title('Time vs Velocity Plot')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (mm/s)')
plt.grid(True)
plt.savefig("C:/Users/Viktor/GOPH_420/repos/goph420_w2025_lab01_stVP/figures/Raw_data.png")



