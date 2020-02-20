import mpl_toolkits.mplot3d as p3
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.integrate import odeint
from matplotlib.animation import ArtistAnimation

N = 200 
t = np.linspace(0, 1, N)

def move_func(s, t):
    v_x, x, v_y, y , z, v_z = s
    dxdt = v_x
    dv_xdt = (x/(a**2))*(g-((v_x**2)/a**2)-((v_y*2)/b**2)-((v_z*2)/c**2))/(((x**2)/a**4) + ((y**2)/b**4) + ((z**2)/c**4))
    
    dydt = v_y
    dv_ydt = (y/(b**2))*(g-((v_x**2)/a**2)-((v_y*2)/b**2)-((v_z*2)/c**2))/(((x**2)/a**4) + ((y**2)/b**4) + ((z**2)/c**4))
    
    dzdt = v_z
    dv_zdt = - g + (x/(a**2))*(g-((v_x**2)/a**2)-((v_y*2)/b**2)-((v_z*2)/c**2))/(((x**2)/a**4) + ((0**2)/b**4) + ((z**2)/c**4))
    
    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

a = 3
b = 2
c = 1

x0 = 1
v_x0 = 0

y0 = 0
v_y0 = 0

z0 = 3
v_z0 = 0

s0 = x0, v_x0, y0, v_y0, z0, v_z0

g = 9.81

sol = odeint(move_func, s0, t)
fig = plt.figure()
ax = p3.Axes3D(fig)

ball, = ax.plot(sol[:,0], sol[:,2], sol[:,4], 'o', color='b')
line, = ax.plot(sol[:,0], sol[:,2], sol[:,4], '-', color='b')

def animation_func(i):
    ball.set_data(sol[i,0],sol[i,2])
    ball.set_3d_properties(sol[i,4])
    
    line.set_data(sol[:i,0], sol[:i,2])
    line.set_3d_properties(sol[:i,4])

ax.set_xlim3d([-2, 2])
ax.set_xlabel('X')

ax.set_ylim3d([-2, 2])
ax.set_ylabel('Y')

ax.set_zlim3d([-2, 2])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, animation_func, N, interval=50)
ani.save('1ani.gif')





















