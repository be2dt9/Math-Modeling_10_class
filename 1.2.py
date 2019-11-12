import matplotlib.pyplot as plt
import numpy as np
def astroida_plotter(t=3,R=2):
    t = np.arange(-10,10,0.1)
    x = R*(np.cos(t))**3
    y = R*(np.sin(t))**3
    plt.plot(x,y)
    plt.show()
astroida_plotter()   