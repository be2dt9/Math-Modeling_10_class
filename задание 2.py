import matplotlib.pyplot as plt
import numpy as np
def parabola(a=1,b=2,c=4):
    '''x**2*a + x*b + c = y
    строит параболу по трем пере-м
    '''
    x = np.arange(-10,10,1)
    y = x**2*a + x*b + c
    plt.plot(x,y)
    plt.show()
parabola()    
    