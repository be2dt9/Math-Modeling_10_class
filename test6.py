import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

#корыто
fig = plt.figure()
ax = p3.Axes3D(fig)

N = 100

y05 = np.linspace(0,5,N)
theta = np.linspace(-np.pi,0,N)
r = 1

x1 = np.outer(np.ones(np.size(y05)), np.cos(theta)) * r
y1 = np.outer(y05, np.ones(np.size(theta)))
z1 = np.outer(np.ones(np.size(y05)), np.sin(theta)) * r

ax.plot_surface(x1,y1,z1,color='g')
plt.show
