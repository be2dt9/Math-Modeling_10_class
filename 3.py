import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

#переменные велечины
start = 10**(-7)
finish = 1.3*10**(-7)
promej = 10**(-9)
t = np.arange(start,finish,promej)
#опреде функцию для си-мы диф. ур-ий
def move_func(s, t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4) = s
     
     #динамика первого тела под 2 и 3 и 4
    dxdt1 = v_x1
    dv_xdt1 = (- G * m2 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               - G * m3 * (x1 - x3) / ((x1 - x3)**2  + (y1 - y3)**2)**1.5
               - G * m4 * (x1 - x4) / ((x1 - x4)**2  + (y1 - y4)**2)**1.5
               + k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 -y2)**2)**1.5
               + k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
               + k * q1 * q4 / m1 * (x1 - x4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5)
    dydt1 = v_y1
    dv_ydt1 = (- G * m2 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               - G * m2 * (y1 - y3) / ((x1 - x3)**2  + (y1 - y3)**2)**1.5
               - G * m2 * (y1 - y4) / ((x1 - x4)**2  + (y1 - y4)**2)**1.5
               + k * q1 * q2 / m1 * (y1 - y2) / ((x1 - x2)**2 + (y1 -y2)**2)**1.5
               + k * q1 * q3 / m1 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
               + k * q1 * q4 / m1 * (y1 - y4) / ((x1 - x4)**2 + (y1 -y4)**2)**1.5)
     #динамика второго  тела под 1 и 3 и 4
    dxdt2 = v_x2
    dv_xdt2 = (- G * m1 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               - G * m3 * (x2 - x3) / ((x2 - x3)**2  + (y2 - y3)**2)**1.5
               - G * m4 * (x2 - x4) / ((x2 - x4)**2  + (y2 - y4)**2)**1.5
               + k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1)**2 + (y2 -y1)**2)**1.5
               + k * q2 * q3 / m2 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
               + k * q2 * q4 / m2 * (x2 - x4) / ((x2 - x4)**2 + (y2 -y4)**2)**1.5) 
    dydt2 = v_y2
    dv_ydt2 = (- G * m1 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               - G * m3 * (y2 - y3) / ((x2 - x3)**2  + (y2 - y3)**2)**1.5
               - G * m4 * (y2 - y4) / ((x2 - x4)**2  + (y2 - y4)**2)**1.5
               + k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 -y1)**2)**1.5
               + k * q2 * q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
               + k * q2 * q4 / m2 * (y2 - y4) / ((x2 - x4)**2 + (y2 -y4)**2)**1.5)
     #динамика третьего  тела под 1 и 2 и 4
    dxdt3 = v_x3
    dv_xdt3 = (- G * m1 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               - G * m2 * (x3 - x2) / ((x3 - x2)**2  + (y3 - y2)**2)**1.5
               - G * m4 * (x3 - x4) / ((x3 - x4)**2  + (y3 - y4)**2)**1.5
               + k * q3 * q1 / m3 * (x3 - x1) / ((x3 - x1)**2 + (y3 -y1)**2)**1.5
               + k * q3 * q2 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
               + k * q3 * q4 / m3 * (x3 - x4) / ((x3 - x4)**2 + (y3 -y4)**2)**1.5)
    dydt3 = v_y3
    dv_ydt3 = (- G * m1 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               - G * m2 * (y3 - y2) / ((x3 - x2)**2  + (y3 - y2)**2)**1.5
               - G * m4 * (y3 - y4) / ((x3 - x4)**2  + (y3 - y4)**2)**1.5
               + k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1)**2 + (y3 -y1)**2)**1.5
               + k * q3 * q2 / m3 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
               + k * q3 * q4 / m3 * (y3 - y4) / ((x3 - x4)**2 + (y3 - y4)**2)**1.5)
     #динамика четвертого  тела под 1 и 2 и 3
    dxdt4 = v_x4
    dv_xdt4 = (- G * m1 * (x4 - x1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
               - G * m2 * (x4 - x2) / ((x4 - x2)**2  + (y4 - y2)**2)**1.5
               - G * m3 * (x4 - x3) / ((x4 - x3)**2  + (y4 - y3)**2)**1.5
               + k * q4 * q1 / m4 * (x4 - x1) / ((x4 - x1)**2 + (y4 -y1)**2)**1.5
               + k * q4 * q2 / m4 * (x4 - x2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5
               + k * q4 * q3 / m4 * (x4 - x3) / ((x4 - x3)**2 + (y4 -y3)**2)**1.5)
    dydt4 = v_y4
    dv_ydt4 = (- G * m1 * (y4 - y1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
               - G * m2 * (y4 - y2) / ((x4 - x2)**2  + (y4 - y2)**2)**1.5
               - G * m3 * (y4 - y3) / ((x4 - x3)**2  + (y4 - y3)**2)**1.5
               + k * q4 * q1 / m3 * (y4 - y1) / ((x4 - x1)**2 + (y4 -y1)**2)**1.5
               + k * q4 * q2 / m3 * (y4 - y2) / ((x4 - x2)**2 + (y4 - y2)**2)**1.5
               + k * q4 * q3 / m3 * (y4 - y3) / ((x4 - x3)**2 + (y4 - y3)**2)**1.5)
    return (dxdt1, dv_xdt1, dydt1, dv_ydt1,
            dxdt2, dv_xdt2, dydt2, dv_ydt2,
            dxdt3, dv_xdt3, dydt3, dv_ydt3,
            dxdt4, dv_xdt4, dydt4, dv_ydt4)
     
 #определяем нач значения и параметры
 
a = 0.008
v = 4*10**6 

x10 = a
v_x10 = v * np.cos(2.35619) #135
y10 = a
v_y10 = v * np.sin(2.35619) 

x20 = -a
v_x20 = v * np.cos(3.92699) #225
y20 = a
v_y20 = v * np.sin(3.92699)

x30 = -a
v_x30 = v * np.cos(5.49779) #315
y30 = -a
v_y30 = v * np.sin(5.49779) #315

x40 = a
v_x40 = v * np.cos(0.785398) #45
y40 = -a
v_y40 = v * np.sin(0.785398) #45

     
s0 = (x10, v_x10,y10,v_y10,
      x20, v_x20,y20,v_y20,
      x30, v_x30,y30,v_y30,
      x40, v_x40,y40,v_y40)    
m1 = 1.1*10**(-27)
q1 = 1.1*10**(-13)

m2 = 1.1*10**(-27)
q2 = 1.1*10**(-13)

m3 = 1.1*10**(-27)
q3 = 1.1*10**(-13)

m4 = 1.1*10**(-27)
q4 = 1.1*10**(-13)

G = 0#6.67 * 10**(-11)
k = 8.98755 * 10**9
# решаем с-му ур-ий
sol = odeint(move_func, s0, t)
# строрим решение в виде графика
fig = plt.figure()
bodys = []
for i in range(0, len(t), 1):
    body1, = plt.plot(sol[:i,0], sol[:i,2],'-',color='r')
    body1_line, = plt.plot(sol[:i,0], sol[:i,2],'-',color='r')
    
    body2, = plt.plot(sol[:i,4], sol[:i,6],'-',color='g')
    body2_line, = plt.plot(sol[:i,4], sol[:i,6],'-',color='g')
    
    body3, = plt.plot(sol[:i,8], sol[:i,10],'-',color='b')
    body3_line, = plt.plot(sol[:i,8], sol[:i,10],'-',color='b')
    
    body4, = plt.plot(sol[:i,12], sol[:i,14],'-',color='m')
    body4_line, = plt.plot(sol[:i,12], sol[:i,14],'-',color='m')
    
    bodys.append([body1,body1_line,body2,body2_line,body3,body3_line,body4,body4_line])
ani = ArtistAnimation(fig, bodys, interval=20)
plt.axis('equal')
ani.save("3.gif")