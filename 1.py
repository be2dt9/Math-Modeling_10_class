from sympy import *

f = Function('f')
x = Function('x')
y = Function('y')
z = Function('z')

t = Symbol('t')
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')

f = (x(t)**2)/a**2 + (y(t)**2)/b**2 + (z(t)**2)/c**2 - 1

print(diff(f,x(t)))
print()
print(diff(f,y(t)))
print()

print(diff(f,z(t)))
print()
print(diff(f,t))
print()
print(diff(diff(f, t), t))
