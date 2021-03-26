"""
@author: capab
This a program to plot a Rossller atractor.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import uniform

def Rossler(x, y, z, a, b, c):
    return [-y-z, x+a*y, b + z*(x-c)]
  
def runge(x0, y0, z0, a, b, c, delta):
    eq = Rossler(x0, y0, z0, a, b, c)    
    k1 = [eq[0]*delta, eq[1]*delta, eq[2]*delta]
    eq2 = Rossler(x0+(k1[0]/2), y0+(k1[1]/2), z0+(k1[2]/2), a, b, c)
    k2 = [eq2[0]*delta, eq2[1]*delta, eq2[2]*delta]
    eq3 = Rossler(x0+(k2[0]/2), y0+(k2[1]/2), z0+(k2[2]/2), a, b, c)
    k3 = [eq3[0]*delta, eq3[1]*delta, eq3[2]*delta]
    eq4 = Rossler(x0+(k3[0]), y0+(k3[1]), z0+(k3[2]), a, b, c)
    k4 = [eq4[0]*delta, eq4[1]*delta, eq4[2]*delta]
    return [x0 + (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6, y0 + (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6, z0 + (k1[2] + 2*k2[2] + 2*k3[2] + k4[2])/6]

""" curvas """  
delta = 0.1

def curva(x0, y0, z0, t0, a, b, c, delta):
    curvax = []
    curvay = []
    curvaz = []   
    while t0 <= 1000 :
        curvax.append(x0)
        curvay.append(y0)
        curvaz.append(z0)
        t0 = t0 + delta
        cur = runge(x0, y0, z0, a, b, c, delta)
        x0= cur[0]
        y0= cur[1]
        z0= cur[2]
    return [curvax, curvay, curvaz]

C = curva(5, -5, 5, 0, 0.2, 0.2, 5.7, 0.01)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(C[0], C[1], C[2])
