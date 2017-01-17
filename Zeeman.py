# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:16:03 2017

@author: Nora
"""


import numpy as np
import matplotlib.pyplot as plt
from excelreadZeeman import machliste

#-------------------------Daten---------------------

"""Spannungsmessung Flipspule"""
Uplus=4.303	
Uminus=4.235
U=(Uplus+Uminus)/2

"""Abstand Drehpunkt zu Drehachse, in cm"""

s=[22.95, 23.0, 23.1, 23.05, 22.95]
s=np.array(s)

mean_s=np.mean(s)
error_s=np.std(s)

#------------------------Gelb--------------------
"""Abstand Zwischen Spektrallinien A"""
A2plus = np.array([11.35, 11.36, 11.31, 11.29, 11.14, 11.07, 11.06, 11.05])
A2 = np.array([11.26, 11.16, 11.14, 11.13, 10.91, 10.85, 10.9, 10.86])
A2minus = np.array([10.86, 10.87, 10.77, 10.8, 10.6, 10.58, 10.54, 10.53])

A1plus = np.array([9.2, 9.15, 9.12, 9.07, 9.08, 9.07, 9.05, 9.02])
A1 = np.array([9.01, 8.95, 8.9, 8.92, 8.8, 8.75, 8.71, 8.76])
A1minus = np.array([8.56, 8.57, 8.47, 8.46, 8.34, 8.29, 8.28, 8.21])

A0plus = np.array([6.27, 6.26, 6.26, 6.19, 6.5, 6.42, 6.42, 6.35])
A0 = np.array([6.0, 6.05, 5.85, 5.86, 6.03, 5.97, 5.97, 5.91])
A0minus= np.array([5.34, 5.24, 5.25, 5.26, 5.29, 5.21, 5.14, 5.11])

A2plus *= 10**(-3)
A2 *= 10**(-3)
A2minus *= 10**(-3)

A1plus *= 10**(-3)
A1 *= 10**(-3)
A1minus *= 10**(-3)

A0plus *= 10**(-3)
A0 *= 10**(-3)
A0minus *= 10**(-3)

meanA2plus = np.mean(A2plus)
meanA2 = np.mean(A2)
meanA2minus = np.mean(A2minus)

meanA1plus = np.mean(A1plus)
meanA1 = np.mean(A1)
meanA1minus = np.mean(A1minus)

meanA0plus = np.mean(A0plus)
meanA0 = np.mean(A0)
meanA0minus = np.mean(A0minus)

errA2plus = np.std(A2plus)
errA2 = np.std(A2)
errA2minus = np.std(A2minus)

errA1plus = np.std(A1plus)
errA1 = np.std(A1)
errA1minus = np.std(A1minus)

errA0plus = np.std(A0plus)
errA0 = np.std(A0)
errA0minus = np.std(A0minus)

#------------------------Blau-----------



#------------------------Funktionen------------------


"""Zwischenwinkel Theta"""
def theta(A,S):
    return np.arctan(A/(2*S))
  
    
"""Ordnung des Hauptmaximum M"""

def Ordnung(d,n0,lam, theta):  #d = Dicke der Lummerplatte, n0 = brechungsindex der Lummerplatte 
                        #lam=wellenlänge unabgelenkt theta= winkel unabgelenkt
    return 2*d/lam*np.sqrt(n0**2-1+(np.sin(theta))**2)
    
"""Frequenzänderung Deltanu  durch Zeemanaufspaltung"""
def deltanu(thetaplus, thetaminus, lam0, M, n0, dn, c, d): #la
    return -c/lam0**2*(np.sin(thetaplus)**2-np.sin(thetaplus)**2)/(lam0*M**2/d**2-4*n0*dn)
    
"""B Feld"""
def BFeld(U,a,N):               #U=gemessene Spannung, a=Fläche der Spule N = Anzahl Wicklungen
    return U/(314.16*a*N)

    
"""Lande'sche g-Faktor"""

def gj(deltanu,B,h,muB,deltamj):
    return (h*deltanu)/(muB*B*deltamj)

#-----------Berechnungen----------

S=mean_s* 10**(-2)

d=3.213*10**(-3)
n0=1.5144
lam0gelb=585.249*10**(-9)

dn=-(1.525-1.510)/(685-400)*10**9
c=2.99*10**8


spuledurchmesser=19.98*10**(-3)
drahtdurchmesser=0.06*10**(-3)
radius=spuledurchmesser/2+drahtdurchmesser/2
a=radius**2*np.pi
N=127

h=6.626 * 10**(-34)
muB=9.247 * 10**(-24)
deltamj=1

"""Theta"""

theta2plus = theta(meanA2plus,S)
theta2 = theta(meanA2,S)
theta2minus = theta(meanA2minus,S)

theta1plus = theta(meanA1plus,S)
theta1 = theta(meanA1,S)
theta1minus = theta(meanA1minus,S)

theta0plus = theta(meanA0plus,S)
theta0 = theta(meanA0,S)
theta0minus = theta(meanA0minus,S)


"""M"""

M2 = Ordnung(d,n0,lam0gelb, theta2)
M1 = Ordnung(d,n0,lam0gelb, theta1)
M0 = Ordnung(d,n0,lam0gelb, theta0)

"""deltanu"""
dnu=deltanu(theta2plus,theta2minus, lam0gelb, M2, n0, dn, c, d)

B=BFeld(U,a,N)

lande=gj(dnu,B,h,muB,deltamj)

print(theta2plus,theta2minus, lam0gelb, M2, n0, dn, c, d)