import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
ball, = plt.plot([],[],'o')
def astroida_plotter(R, t):
    x = R*(np.cos(t))**3
    y = R*(np.sin(t))**3
    return x, y
edge = 4
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(frame):
    ball.set_data(astroida_plotter(R=3, t=frame))
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=np.arange(0,2*np.pi,10),
                              interval=100)
ani.save('ani1.gif')