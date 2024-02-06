#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:31:37 2024

@author: austin
"""
import numpy as np

A = int(input("Enter a value between 0-1: ")) #A[0]
B = int(input("Enter a value between 0-1: ")) #B[1]
C = int(input("Enter a value between 0-1: ")) #C[2]
D = int(input("Enter a value between 0-1: ")) #D[3]

inputs = np.array([A,B,C,D])
inputs = np.clip(inputs,0,1)
print(inputs)

out1 = not np.logical_or(inputs[0],inputs[1]) 
out2 = not np.logical_and(out1,inputs[2]) #AB NAND C

inputs[3] = np.logical_not(inputs[3])

out3 = np.logical_and(inputs[2], inputs[3]) #C AND D

out = np.logical_or(out2, out3)

print(out)
