import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
fig = plt.figure()
x_coord = np.linspace(0,10,100)
y_coord = np.zeros(100)
anim_list = []
def enge(0,100,1):
    anim_object, = plt.plot(x_coord[i],y_coord[i],'o')
    anim_list.append([anim_object])
ani = ArtistAnimation(fig,anim_list,interval=50)
ani.save('ani.gif')  

