import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig = plt.figure()
x = np.linspace(-5,5,100)
def circle_func(x_centre_point,
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

t = np.linspace(0,4*np.pi,100)
R = 5
cycloid_x = R*(t - np.sin(t))
cycloid_y = R*(1 - np.cos(t))
x_centre_move = R*t
anim_list = []
N = 100
for i in range(0,N,1):
    x,y = circle_func(cycloid_x[i],cycloid_y[i],R=R,N=N)
    circle, = plt.plot(x,y,'g-',lw=2)
    cycloid, = plt.plot(cycloid_x[i],cycloid_y[i],'r-',lw=2)
    point, = plt.plot(cycloid_x[i],cycloid_y[i])
    anim_list.append([circle,cycloid,point])
    plt.axis('equal')
        
    
ani = ArtistAnimation(fig,anim_list,interval=50)
ani.save('ani2.gif')  
