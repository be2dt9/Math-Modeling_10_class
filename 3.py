from constans import m,h,v,g
import numpy as np
def full_mech_energ(m,h,v):
    F = (m*v**2)/2 + m*g*h
    return(F)
print(full_mech_energ(m,h,v))
