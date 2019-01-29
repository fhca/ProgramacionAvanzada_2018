import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-4*np.pi, 4*np.pi, 100)
y = np.linspace(-4*np.pi, 4*np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X)*np.cos(Y)
ax.plot_surface(X, Y, Z, cmap=cm.RdBu, linewidth=0, antialiased=False)

plt.show()
