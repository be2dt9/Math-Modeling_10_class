import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0,100,1)
def speedup_function(v,t):
    savisspeed = f/m - (k*v**2)/m
    return savisspeed
v = 0
f = 10
k = 0.5
m = 100
solve_speed = odeint(speedup_function,v,t)
plt.plot(t,solve_speed[:,0],label='измение скорости')
plt.legend()
plt.show()