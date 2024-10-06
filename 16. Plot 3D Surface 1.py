import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(X, Y)
def f(x, y):
 return (1 - y**5 + x**5) * np.exp(-x**2 - y**2)
Z = f(X, Y)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
plt.show()
