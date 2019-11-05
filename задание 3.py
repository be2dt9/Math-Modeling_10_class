import matplotlib.pyplot as plt
import numpy as np

def ellips_plotter(a=3, b=2):
    """строит эллипс по двум пере-м
    """
    x = np.arange(-2*a,2*a,0.1)
    y = np.arange(-2*a,2*a,0.1)
    X,Y = np.meshgrid(x,y)
    fxy = (X**2)/(a**2) + (Y**2)/(b**2)
    plt.contour(X, Y, fxy, levels=[1])
    plt.show()
    
ellips_plotter()