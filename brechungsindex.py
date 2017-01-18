# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
colour = 0 #0 = gelb, 1=blau

def dndlam(n,lam):
    #gibt Steigung mit Fehler zurück in m
    n0 = 1.510
    lam0 = 400
    a = []
    for i in range(2):
        dn = (n[i]-n0)/(lam0-lam[i])*10**9
        a.append(dn)
    sigma = a[0]-np.mean(a)
    return np.mean(a),sigma

if colour == 0:
    n = [1.5242, 1.5232]
    lam = [673,684]
else:
    n = [1.5260,1.5254]
    lam = [651,660]

print(dndlam(n,lam))