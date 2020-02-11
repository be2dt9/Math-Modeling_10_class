import mpl_toolkits.mplot3d as p3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0,2 * np.pi, 100)
theta = np.linspace(0, 4*np.pi, 100)
a = 1
b = 2
c = 3

x = a * np.outer(np.cos(phi), np.sinh(theta))
y = b * np.outer(np.sin(phi), np.sinh(theta))
z = c * np.outer(np.ones(np.size(phi)), np.sinh(theta))

ax.plot_surface(x, y, z, color='r')

a = 1
b = 2
c = -3

x = a * np.outer(np.cos(phi), np.sinh(theta))
y = b * np.outer(np.sin(phi), np.sinh(theta))
z = c * np.outer(np.ones(np.size(phi)), np.sinh(theta))

ax.plot_surface(x, y, z, color='r')
plt.show()