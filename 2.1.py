import mpl_toolkits.mplot3d as p3
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation

N = 300 
t = np.linspace(0, 5, N)

def move_func(s, t):
    x, v_x, y ,v_y, z , v_z = s
    
    dxdt = v_x
    dv_xdt = 3*g*z/(z**2+x**2)*x
    
    dydt = v_y
    dv_ydt = 0
    
    dzdt = v_z
    dv_zdt = -g + 3*g*z/(z**2+x**2)*z
    
    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt


x0 = 1
v_x0 = 0

y0 = 0
v_y0 = 1

z0 = 0
v_z0 = 0

s0 = x0, v_x0, y0, v_y0, z0, v_z0

g = 9.81

sol = odeint(move_func, s0, t)
#шар линия
fig = plt.figure()
ax = p3.Axes3D(fig)

ball, = ax.plot(sol[:,0], sol[:,2], sol[:,4], 'o', color='b')
line, = ax.plot(sol[:,0], sol[:,2], sol[:,4], '-', color='b')
# корыто
fig = plt.figure()
ax = p3.Axes3D(fig)
N1 = 300
theta = np.linspace(0,4*np.pi,N1)
r = 1

x1 = np.outer(np.ones(np.size(y1)), np.cos(theta))*r
y1 = np.linspace(0,10,N1)
z1 =  np.outer(np.ones(np.size(y1)), np.sin(theta))*r

ax.plot_surface(x1,y1,z1,color='g')


def animation_func(i):
    ball.set_data(sol[i,0],sol[i,2])
    ball.set_3d_properties(sol[i,4])
    
    line.set_data(sol[:i,0], sol[:i,2])
    line.set_3d_properties(sol[:i,4])

ax.set_xlabel('X')

ax.set_ylabel('Y')

ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, animation_func, N, interval=50)
ani.save('ani2-1.gif')