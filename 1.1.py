import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig = plt.figure()
def parabola_func(x_centre_point,
                y_centre_point,
                R,
                N):
    x = np.zeros(N)
    y = np.zeros(N)
    for i in range (0,N,1):
        alpha = np.linspace(0,2*np.pi,N)
        x[i] = x_centre_point + R*np.cos(alpha[i])
        y[i] = y_centre_point + R*np.sin(alpha[i])
    return x,y

parabola_x = np.linspace(0,10,100)
parabola_y = parabola_x**2 + parabola_x 


anim_list = []
N = 1
for i in range(0,N,1):
    x,y = parabola_func(parabola_x[i],parabola_y,R=1,N=N)
    circle, = plt.plot(x,y,'g-',lw=2)
# =============================================================================
#     parabola, = plt.plot(parabola_x[i],parabola_y[i],'r-',lw=2)
#     point, = plt.plot(parabola_x[i],parabola_y[i])
# =============================================================================
    anim_list.append([circle])
    
        
    
ani = ArtistAnimation(fig,anim_list,interval=50)
ani.save('ani.gif')  
