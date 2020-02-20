import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

N = 300

y1 = np.linspace(0,10,N)
theta = np.linspace(0,2*np.pi,N)

r = 10

x1 = np.outer(np.ones(np.size(y1)), np.cos(theta))
y1 = np.outer(y1, np.ones(np.size(theta)))
z1 = np.outer(np.ones(np.size(y1)), np.sin(theta))

ax.plot_surface(x1,y1,z1,color='g')

plt.show()