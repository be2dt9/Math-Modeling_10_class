import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = np.arange(0,4,1)
#созданеи диф-ой функции 
def investlost_function(m,t):
    moneylost = -k * m * t
    return moneylost
m_0 = 1000
k = 0.08
solve_money = odeint(investlost_function,m_0,t)
plt.plot(t,solve_money[:,0],label='инвестиции')
plt.legend()
plt.show()