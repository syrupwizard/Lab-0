#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:53:50 2024

@author: austin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math as m

###triangle coords

A = np.array([0,0])
B = np.array([0,1])
C = np.array([1,0])

tri = np.array([A,B,C])


###scalars
Sx = float(input('Enter scalar Sx: '))
Sy = float(input('Enter scalar Sy: '))
Ts = np.array([[Sx,0],
               [0,Sy]])

###rotation
rotation = float(input('Enter rotation angle in degrees: '))
rotation = np.radians(rotation)

Tr = np.array([ [m.cos(rotation),-(m.sin(rotation))],
                [m.sin(rotation),m.cos(rotation)]
                       ])

###matrix multiplication of two transformations
T = np.matmul(Tr,Ts)

###matrix multiplications of original coords with transform matrix T
Af = np.matmul(T,A)
Bf = np.matmul(T,B)
Cf = np.matmul(T,C)

###final transformed matrix
transformed_tri = np.array([Af,Bf,Cf])

###print original tri
tri = Polygon(tri)
ax = plt.gca()
ay = plt.gca()
ax.add_patch(tri)

plt.xlim(-Sx,Sx)
plt.ylim(-Sy,Sy)
plt.show()

###pause between printing
input("Press enter for transformation")

###print transformed tri
transformed_tri = Polygon(transformed_tri)
ax = plt.gca()
ay = plt.gca()

ax.add_patch(transformed_tri)
plt.xlim(-Sx,Sx)
plt.ylim(-Sy,Sy)
plt.show()


###test code
"""print('Triangle\n', A, B, C)
print()

print('Scalar plot', Ts)
print()

print('Rotation', Tr)
print()

print('Tr * Ts', T)
print()

print('Transformed Triangle\n', Af, Bf, Cf)"""

