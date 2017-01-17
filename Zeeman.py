# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:16:03 2017

@author: Nora
"""


import numpy as np
import matplotlib.pyplot as plt
from excelreadZeeman import machliste

#-------------------------Farbe---------------------

farbe = y

if farbe == y:
    lam0 = 585.249e-9
    n0 = 1.5145
    
    A2plus = np.array([11.35, 11.36, 11.31, 11.29])*10**(-3)
    A2 = np.array([11.26, 11.16, 11.14, 11.13])*10**(-3)
    A2minus = np.array([10.86, 10.87, 10.77, 10.8])*10**(-3)

    A1plus = np.array([9.2, 9.15, 9.12, 9.07])*10**(-3)
    A1 = np.array([9.01, 8.95, 8.9, 8.92])*10**(-3)
    A1minus = np.array([8.56, 8.57, 8.47, 8.46])*10**(-3)

    A0plus = np.array([6.27, 6.26, 6.26, 6.19])*10**(-3)
    A0 = np.array([6.0, 6.05, 5.85, 5.86])*10**(-3)
    A0minus= np.array([5.34, 5.24, 5.25, 5.26])*10**(-3)
    
elif farbe == b:
    lam0 = 540.056e-9
    n0 = 1.5172
    
    A2plus = np.array([11.14, 11.07, 11.06, 11.05])*10**(-3)
    A2 = np.array([10.91, 10.85, 10.9, 10.86])*10**(-3)
    A2minus = np.array([10.6, 10.58, 10.54, 10.53])*10**(-3)

    A1plus = np.array([9.08, 9.07, 9.05, 9.02])*10**(-3)
    A1 = np.array([8.8, 8.75, 8.71, 8.76])*10**(-3)
    A1minus = np.array([8.34, 8.29, 8.28, 8.21])*10**(-3)

    A0plus = np.array([6.5, 6.42, 6.42, 6.35])*10**(-3)
    A0 = np.array([6.03, 5.97, 5.97, 5.91])*10**(-3)
    A0minus= np.array([5.29, 5.21, 5.14, 5.11])*10**(-3)



#-------------------------A berechnen---------------------

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



#-------------------------Daten---------------------

"""Spannungsmessung Flipspule"""
Uplus=4.303	
Uminus=4.235
U=(Uplus+Uminus)/2

"""Drehachse in cm"""

s=[22.95, 23.0, 23.1, 23.05, 22.95]
s=np.array(s)
S=np.mean(s)


#------------------------Funktionen------------------


"""Zwischenwinkel Theta"""
def theta(A,S):
    return np.arctan(A/(2*S))
  
    
"""Ordnung des Hauptmaximum M"""

def Ordnung(d,n0,lam0, theta):  #d = Dicke der Lummerplatte, n0 = brechungsindex der Lummerplatte 
                                #lam=wellenlänge unabgelenkt theta= winkel unabgelenkt
    return 2*d/lam0*np.sqrt(n0**2-1+(np.sin(theta))**2)
    
"""Frequenzänderung Deltanu  durch Zeemanaufspaltung"""
def deltanu(thetaplus, thetaminus, lam0, M, n0, dn, c, d): #la
    return -c/lam0**2*(np.sin(thetaplus)**2-np.sin(thetaminus)**2)/(lam0*M**2/d**2-4*n0*dn)
    
"""B Feld"""
def BFeld(U,F,N):               #U=gemessene Spannung, F=Fläche der Spule N = Anzahl Wicklungen
    return U/(314.16*F*N)

    
"""Lande'sche g-Faktor"""

def gj(deltanu,B,h,muB,deltamj):
    return (h*deltanu)/(muB*B*deltamj)

#-----------Berechnungen----------

S=mean_s* 10**(-2)

d=3.213*10**(-3)
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

M2 = Ordnung(d,n0,lam0, theta2)
M1 = Ordnung(d,n0,lam0, theta1)
M0 = Ordnung(d,n0,lam0, theta0)

"""deltanu"""
dnu2 = deltanu(theta2plus,theta2minus, lam0, M2, n0, dn, c, d)
dnu1 = deltanu(theta1plus,theta1minus, lam0, M2, n0, dn, c, d)
dnu0 = deltanu(theta0plus,theta0minus, lam0, M2, n0, dn, c, d)

B = BFeld(U,a,N)

lande2 = gj(dnu2,B,h,muB,deltamj)
lande1 = gj(dnu1,B,h,muB,deltamj)
lande0 = gj(dnu0,B,h,muB,deltamj)


print(lande2,lande1,lande0)


#-------------------------Ableitungen---------------------

def dthetadA(A,S):
    return 2*S/(A**2+(2*S)**2)

def dthetadS(A,S):
    return -2*A/(A**2+(2*S)**2)

def dMdd(d,n0,theta,lam0):
    return 2/lam0 * (n0**2-1+(np.sin(theta))**2)**(1/2)

def dMdn0(d,n0,theta,lam0):
    return 2*d*n0/lam0 * (n0**2-1+(np.sin(theta))**2)**(-1/2)

def dMdtheta(d,n0,theta,lam0):
    return d*np.sin(2*theta)/lam0 * (n0**2-1+(np.sin(theta))**2)**(-1/2)

def dnudthetaplus(thetaplus,thetaminus,M,d,n0,dn,c,lam0):
    return -c*np.sin(2*thetaplus)/lam0**2 * (lam0*M**2/d**2-4*n0*dn)**(-1)

def dnudthetaminus(thetaplus,thetaminus,M,d,n0,dn,c,lam0):
    return c*np.sin(2*thetaminus)/lam0**2 * (lam0*M**2/d**2-4*n0*dn)**(-1)

def dnudM(thetaplus,thetaminus,M,d,n0,dn,c,lam0):
    return c*((np.sin(thetaplus))**2-(np.sin(thetaminus))**2)/lam0 * 2*M/d**2 * (lam0*M**2/d**2-4*n0*dn)**(-2)

def dnudd(thetaplus,thetaminus,M,d,n0,dn,c,lam0):
    return -c*((np.sin(thetaplus))**2-(np.sin(thetaminus))**2)/lam0 * 2*M**2/d**3 * (lam0*M**2/d**2-4*n0*dn)**(-2)

def dnudn0(thetaplus,thetaminus,M,d,n0,dn,c,lam0):
    return -c*((np.sin(thetaplus))**2-(np.sin(thetaminus))**2)/lam0**2 * 4*dn * (lam0*M**2/d**2-4*n0*dn)**(-2)

def dnuddn(thetaplus,thetaminus,M,d,n0,dn,c,lam0):
    return -c*((np.sin(thetaplus))**2-(np.sin(thetaminus))**2)/lam0**2 * 4*n0 * (lam0*M**2/d**2-4*n0*dn)**(-2)

def dBdU(U,A,N):
    return 1/(314.16*A*N)

def dBdA(U,A,N):
    return -U/(314.16*A**2*N)

def dgdnu(deltanu,muB,B,deltamj):
    return h/(muB*B*deltamj)

def dgdB(deltanu,muB,B,deltamj):



#-------------------------Fehler---------------------

def uA(ux):
    return np.sqrt((ux*1)**2+(ux*(-1))**2)

def utheta(A,S,uA,uS):
    dA = dthetadA(A,S)
    dS = dthetadS(A,S)
    return np.sqrt((uA*dA)**2+(uS*dS)**2)

def uM(d,n0,theta,lam0,ud,un0,utheta):
    dd = dMdd(d,n0,theta,lam0)
    dn0 = dMdn0(d,n0,theta,lam0)
    dtheta = dMdtheta(d,n0,theta,lam0)
    return np.sqrt((ud*dd)**2+(un0*dn0)**2+(utheta*dtheta)**2)

def unu(thetaplus,thetaminus,M,d,n0,dn,c,lam0,uthetaplus,uthetaminus,uM,ud,un0,udn):
    dthetaplus = dnudthetaplus(thetaplus,thetaminus,M,d,n0,dn,c,lam0)
    dthetaminus = dnudthetaminus(thetaplus,thetaminus,M,d,n0,dn,c,lam0)
    dM = dnudM(thetaplus,thetaminus,M,d,n0,dn,c,lam0)
    dd = dnudd(thetaplus,thetaminus,M,d,n0,dn,c,lam0)
    dn0 = dnudn0(thetaplus,thetaminus,M,d,n0,dn,c,lam0)
    ddn = dnuddn(thetaplus,thetaminus,M,d,n0,dn,c,lam0)
    return np.sqrt((uthetaplus*dthetaplus)**2+(uthetaminus*dthetaminus)**2+(uM*dM)**2+(ud*dd)**2+(un0*dn0)**2+(udn*ddn)**2)

def uB(U,F,N,uU,uF):
    dU = dBdU(U,F,N)
    dA = dBdA(U,F,N)
    return np.sqrt((uU*dU)**2+(uF*dF)**2)

def ug(deltanu,muB,B,deltamj,unu,uB):
    dnu = dgdnu(deltanu,muB,B,deltamj)
    dB = dgdB(deltanu,muB,B,deltamj)
    return np.sqrt((unu*dnu)**2+(uB*dB)**2)



#-------------------------Fehlerrechnung---------------------

ux = 5e-6
uS = np.std(s)
ud = 1e-6
un0 = 1e-4
udn =
uU =
uA = uA(ux)
uF = np.pi*(3e-5)**2

utheta0 = utheta(A0,S,uA,uS)
utheta0plus = utheta(A0plus,S,uA,uS)
utheta0minus = utheta(A0minus,S,uA,uS)

utheta1 = utheta(A1,S,uA,uS)
utheta1plus = utheta(A1plus,S,uA,uS)
utheta1minus = utheta(A1minus,S,uA,uS)

utheta2 = utheta(A2,S,uA,uS)
utheta2plus = utheta(A2plus,S,uA,uS)
utheta2minus = utheta(A2minus,S,uA,uS)

uM0 = uM(d,n0,theta0,lam0,ud,un0,utheta0)
uM1 = uM(d,n0,theta1,lam0,ud,un0,utheta1)
uM2 = uM(d,n0,theta2,lam0,ud,un0,utheta2)

unu0 = unu(theta0plus,theta0minus,M0,d,n0,dn,c,lam0,utheta0plus,utheta0minus,uM0,ud,un0,udn)
unu1 = unu(theta1plus,theta1minus,M1,d,n0,dn,c,lam0,utheta1plus,utheta1minus,uM1,ud,un0,udn)
unu2 = unu(theta2plus,theta2minus,M2,d,n0,dn,c,lam0,utheta2plus,utheta2minus,uM2,ud,un0,udn)

uB = uB(U,F,N,uU,uF)

ug0 = ug(deltanu0,muB,B0,deltamj,unu0,uB)
ug1 = ug(deltanu1,muB,B1,deltamj,unu1,uB)
ug2 = ug(deltanu2,muB,B2,deltamj,unu2,uB)
