from module1 import grP, h, a, B
from numpy import cos,tan
V = ((grP*h*(tan(B)**2))/((2*cos(a)**2)*(1 - tan(B)*tan(a))))**0.5
print(V)