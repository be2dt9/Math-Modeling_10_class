import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0,1000,1)
#созданеи диф-ой функции 
def bio_function(n,t):
    bioploding = k * n
    return bioploding
n_0 = 1
k = 0.02
solve_bio = odeint(bio_function,n_0,t)
plt.plot(t,solve_bio[:,0],label='розомоножение')
plt.show()
    