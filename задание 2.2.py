import matplotlib.pyplot as plt
import numpy as np
def geperbula(d=1):
    '''строит гипербулу 
    '''
    x = np.arange(-10,10,1)
    y = d/x
    plt.plot(x,y)
    plt.show()
geperbula()    