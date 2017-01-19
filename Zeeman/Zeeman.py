# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:16:03 2017

@author: Nora
"""


import numpy as np
import matplotlib.pyplot as plt
#from excelreadZeeman import machliste

#-------------------------Farbe---------------------
#Gelb=1, Blau=0

farbe = 1

print ''

if farbe == 1:
    lam0 = 585.249e-9
    n0 = 1.5145
    un0 = 1e-4
    dn = -49246.8
    udn = 2767.9
    
    print 'Farbe: Gelb'
    A2plus = np.array([11.35, 11.36, 11.31, 11.29])*10**(-3)
    A2 = np.array([11.26, 11.16, 11.14, 11.13])*10**(-3)
    A2minus = np.array([10.86, 10.87, 10.77, 10.8])*10**(-3)

    A1plus = np.array([9.2, 9.15, 9.12, 9.07])*10**(-3)
    A1 = np.array([9.01, 8.95, 8.9, 8.92])*10**(-3)
    A1minus = np.array([8.56, 8.57, 8.47, 8.46])*10**(-3)

    A0plus = np.array([6.27, 6.26, 6.26, 6.19])*10**(-3)
    A0 = np.array([6.0, 6.05, 5.85, 5.86])*10**(-3)
    A0minus= np.array([5.34, 5.24, 5.25, 5.26])*10**(-3)
    
elif farbe == 0:
    lam0 = 540.056e-9
    n0 = 1.5172
    un0 = 1e-4
    dn = -61487.9
    udn = 2257.1
    
    print 'Farbe: Blau-Grün' 
    A2plus = np.array([11.14, 11.07, 11.06, 11.05])*10**(-3)
    A2 = np.array([10.91, 10.85, 10.9, 10.86])*10**(-3)
    A2minus = np.array([10.6, 10.58, 10.54, 10.53])*10**(-3)

    A1plus = np.array([9.08, 9.07, 9.05, 9.02])*10**(-3)
    A1 = np.array([8.8, 8.75, 8.71, 8.76])*10**(-3)
    A1minus = np.array([8.34, 8.29, 8.28, 8.21])*10**(-3)

    A0plus = np.array([6.5, 6.42, 6.42, 6.35])*10**(-3)
    A0 = np.array([6.03, 5.97, 5.97, 5.91])*10**(-3)
    A0minus= np.array([5.29, 5.21, 5.14, 5.11])*10**(-3)



#-------------------------Daten---------------------

"""Spannungsmessung Flipspule"""
Uplus = np.array([4.3, 4.27, 4.29, 4.32, 4.31, 4.29, 4.33, 4.27, 4.34, 4.31])
Uminus = np.array([4.24, 4.23, 4.22, 4.24, 4.22, 4.24, 4.24, 4.24, 4.24, 4.24])
meanUplus = np.mean(Uplus)
meanUminus = np.mean(Uminus)
stdUplus = np.std(Uplus)
stdUminus = np.std(Uminus)

U = (meanUplus+meanUminus) / 2
uU = stdUplus


"""Drehachse in cm"""

s=[22.95, 23.0, 23.1, 23.05, 22.95]
s=np.array(s)*10**(-2)
S=np.mean(s)
uS=np.std(s)



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

# Dicke Lummerplatte und Unsicherheit
d=3.213*10**(-3)
ud = 1e-6
c=2.99*10**8


spuledurchmesser=19.98*10**(-3)
drahtdurchmesser=0.06*10**(-3)
radius=spuledurchmesser/2+drahtdurchmesser/2
F=radius**2*np.pi
uF = (np.pi*(spuledurchmesser/2+drahtdurchmesser)**2-np.pi*(spuledurchmesser/2)**2)
N=127

h=6.626 * 10**(-34)
muB=9.247 * 10**(-24)
deltamj=1


"""A"""

uA2plus = np.std(A2plus)
uA2 = np.std(A2)
uA2minus = np.std(A2minus)

uA1plus = np.std(A1plus)
uA1 = np.std(A1)
uA1minus = np.std(A1minus)

uA0plus = np.std(A0plus)
uA0 = np.std(A0)
uA0minus = np.std(A0minus)

A2plus = np.mean(A2plus)
A2 = np.mean(A2)
A2minus = np.mean(A2minus)

A1plus = np.mean(A1plus)
A1 = np.mean(A1)
A1minus = np.mean(A1minus)

A0plus = np.mean(A0plus)
A0 = np.mean(A0)
A0minus = np.mean(A0minus)





"""Theta"""

theta2plus = theta(A2plus,S)
theta2 = theta(A2,S)
theta2minus = theta(A2minus,S)

theta1plus = theta(A1plus,S)
theta1 = theta(A1,S)
theta1minus = theta(A1minus,S)

theta0plus = theta(A0plus,S)
theta0 = theta(A0,S)
theta0minus = theta(A0minus,S)



"""M"""

M2 = Ordnung(d,n0,lam0, theta2)
M1 = Ordnung(d,n0,lam0, theta1)
M0 = Ordnung(d,n0,lam0, theta0)



"""deltanu"""
deltanu2 = deltanu(theta2plus,theta2minus, lam0, M2, n0, dn, c, d)
deltanu1 = deltanu(theta1plus,theta1minus, lam0, M2, n0, dn, c, d)
deltanu0 = deltanu(theta0plus,theta0minus, lam0, M2, n0, dn, c, d)



"""Lande-Faktoren"""

B = BFeld(U,F,N)

lande2 = gj(deltanu2,B,h,muB,deltamj)
lande1 = gj(deltanu1,B,h,muB,deltamj)
lande0 = gj(deltanu0,B,h,muB,deltamj)




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

def dBdU(U,F,N):
    return 1/(314.16*F*N)

def dBdF(U,F,N):
    return -U/(314.16*F**2*N)

def dgdnu(deltanu,muB,B,deltamj):
    return h/(muB*B*deltamj)

def dgdB(deltanu,muB,B,deltamj):
    return -h*deltanu/(muB*B**2*deltamj)



#-------------------------Fehler---------------------


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
    dF = dBdF(U,F,N)
    return np.sqrt((uU*dU)**2+(uF*dF)**2)

def ug(deltanu,muB,B,deltamj,unu,uB):
    dnu = dgdnu(deltanu,muB,B,deltamj)
    dB = dgdB(deltanu,muB,B,deltamj)
    return np.sqrt((unu*dnu)**2+(uB*dB)**2)



#-------------------------Fehlerrechnung---------------------

utheta0 = utheta(A0,S,uA0,uS)
utheta0plus = utheta(A0plus,S,uA0plus,uS)
utheta0minus = utheta(A0minus,S,uA0minus,uS)

utheta1 = utheta(A1,S,uA1,uS)
utheta1plus = utheta(A1plus,S,uA1plus,uS)
utheta1minus = utheta(A1minus,S,uA1minus,uS)

utheta2 = utheta(A2,S,uA2,uS)
utheta2plus = utheta(A2plus,S,uA2plus,uS)
utheta2minus = utheta(A2minus,S,uA2minus,uS)

uM0 = uM(d,n0,theta0,lam0,ud,un0,utheta0)
uM1 = uM(d,n0,theta1,lam0,ud,un0,utheta1)
uM2 = uM(d,n0,theta2,lam0,ud,un0,utheta2)

unu0 = unu(theta0plus,theta0minus,M0,d,n0,dn,c,lam0,utheta0plus,utheta0minus,uM0,ud,un0,udn)
unu1 = unu(theta1plus,theta1minus,M1,d,n0,dn,c,lam0,utheta1plus,utheta1minus,uM1,ud,un0,udn)
unu2 = unu(theta2plus,theta2minus,M2,d,n0,dn,c,lam0,utheta2plus,utheta2minus,uM2,ud,un0,udn)

uB = uB(U,F,N,uU,uF)

ug0 = ug(deltanu0,muB,B,deltamj,unu0,uB)
ug1 = ug(deltanu1,muB,B,deltamj,unu1,uB)
ug2 = ug(deltanu2,muB,B,deltamj,unu2,uB)



#-------------------------Print---------------------

print ''
print 'Theta0+: (', '%.3f' % (theta0plus*180/np.pi), '+/-', '%.3f' % (utheta0plus*180/np.pi), ') °C'
print 'Theta0: (', '%.3f' % (theta0*180/np.pi), '+/-', '%.3f' % (utheta0*180/np.pi), ') °C'
print 'Theta0-: (', '%.3f' % (theta0minus*180/np.pi), '+/-', '%.3f' % (utheta0minus*180/np.pi), ') °C'
print 'Theta1+: (', '%.3f' % (theta1plus*180/np.pi), '+/-', '%.3f' % (utheta1plus*180/np.pi), ') °C'
print 'Theta1: (', '%.3f' % (theta1*180/np.pi), '+/-', '%.3f' % (utheta1*180/np.pi), ') °C'
print 'Theta1-: (', '%.3f' % (theta1minus*180/np.pi), '+/-', '%.3f' % (utheta1minus*180/np.pi), ') °C'
print 'Theta2+: (', '%.3f' % (theta2plus*180/np.pi), '+/-', '%.3f' % (utheta2plus*180/np.pi), ') °C'
print 'Theta2: (', '%.3f' % (theta2*180/np.pi), '+/-', '%.3f' % (utheta2*180/np.pi), ') °C'
print 'Theta2-: (', '%.3f' % (theta2minus*180/np.pi), '+/-', '%.3f' % (utheta2minus*180/np.pi), ') °C'

print ''
print 'Ordnung M0: (', '%.1f' % M0, '+/-', '%.1f' % uM0, ')'
print 'Ordnung M1: (', '%.1f' % M1, '+/-', '%.1f' % uM1, ')'
print 'Ordnung M2: (', '%.1f' % M2, '+/-', '%.1f' % uM2, ')'

print ''
print 'Delta nu (M0): (', '%.2f' % (-deltanu0/1e9), '+/-', '%.2f' % (unu0/1e9), ') GHz'
print 'Delta nu (M1): (', '%.2f' % (-deltanu1/1e9), '+/-', '%.2f' % (unu1/1e9), ') GHz'
print 'Delta nu (M2): (', '%.2f' % (-deltanu2/1e9), '+/-', '%.2f' % (unu2/1e9), ') GHz'

print ''
print 'B-Feld: (', '%.3f' % (B), '+/-', '%.3f' % (uB), ') T'

print ''
print 'Landé-Faktor (M0): (', '%.3f' % (-lande0), '+/-', '%.3f' % (ug0), ')'
print 'Landé-Faktor (M1): (', '%.3f' % (-lande1), '+/-', '%.3f' % (ug1), ')'
print 'Landé-Faktor (M2): (', '%.3f' % (-lande2), '+/-', '%.3f' % (ug2), ')'
print ''



