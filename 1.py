import matplotlib.pyplot as plt
import numpy as np
def cicloida_plotter(t=3,R=2):
    t = np.arange(-10,10,1)
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
    plt.plot(x,y)
    plt.show()
cicloida_plotter()    
    