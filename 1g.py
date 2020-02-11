import mpl_toolkits.mplot3d as p3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2*np.pi, 100)


x = np.outer(phi, np.cos(theta)) + 2 * (np.ones(np.size(phi)), theta**2)
y = np.outer(phi, np.sin(theta)) + 0.2 * (np.ones(np.size(phi)),theta**2)
z = 1 * np.outer(np.ones(np.size(phi)),theta**2)

ax.plot_surface(x, y, z, color='r')
plt.show()