import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# Data
x = np.arange(8)
y = np.random.randint(0, 10, 8)
y2 = y + np.random.randint(0, 3, 8)
y3 = y2 + np.random.randint(0, 3, 8)
y4 = y3 + np.random.randint(0, 3, 8)
y5 = y4 + np.random.randint(0, 3, 8)
clr = ['#4bb2c5', '#c5b47f', '#EAA228', '#579575', '#839557', '#958c12',
'#953579', '#4b5de4']
# Membuat figure dan axis 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Lebar bar
bar_width = 0.8
# Fungsi untuk plotting bar 3D
def plot_bar3d(x, y, z_base, color):
 ax.bar3d(x, z_base, np.zeros_like(x), bar_width, bar_width, y,
color=color)
# Plot bar 3D dengan zdir sebagai acuan
plot_bar3d(x, y, 0, clr)
plot_bar3d(x, y2, 10, clr)
plot_bar3d(x, y3, 20, clr)
plot_bar3d(x, y4, 30, clr)
plot_bar3d(x, y5, 40, clr)
# Menambahkan label
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
# Menampilkan plot
plt.show()
