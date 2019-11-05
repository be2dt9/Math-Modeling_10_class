import matplotlib.pyplot as plt
import numpy as np
def circler_plotter(r=0.3,title='circle plotter'):
    ''' рисовать окр-сти
    '''
    x = np.arange(-2.0,2.0,0.1)
    y = np.arange(-2.0,2.0,0.1)
    x,y = np.meshgrid(x,y)
    fxy = x**2 + y**2
    plt.contour(x,y,fxy,levels=[r**2])
    plt.show()
circler_plotter()
    