# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:45:49 2017

@author: Nora
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:40:34 2017

@author: Nora
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as curve_fit



#____________________Messdaten_______________________________

serie = 2

if serie == 1:          #Set1 mit Ausreisser
    q = np.array([5.6536, 5.8741, 4.4131, 3.7338, 2.4297, 1.8257])*10**(-3)
    err_q = np.array([0.0349, 0.0343, 0.0268, 0.0217, 0.0137, 0.0103])*10**(-3)

    I = np.array([1000.0, 900.0, 800.0, 700.0, 500.0, 403.0])*10**(-3)
    Tlist = np.array([186.4, 185.0, 185.2, 185.6, 185.8, 185.9])+273

    I2 = np.array([1000.0, 800.0, 700.0, 500.0, 403.0])*10**(-3)
    q2 = np.array([5.6536, 4.4131, 3.7338, 2.4297, 1.8257])*10**(-3)

elif serie == 2:        #Set 2, viel schöner :)
    q = np.array([5.7280,5.3001,4.7840,4.2071,3.5424,2.2464])*10**(-3)
    err_q = np.array([0.0041,0.0032,0.0032,0.0029,0.0025,0.0015])*10**(-3)
    
    I = np.array([1000,900,800,700,600,402])*10**(-3)
    Tlist = np.array([187.5,186.7,186.5,186.5,186.3,184.1])+273
 
 
#______________Berechnung B Feld_______________________

def BFeld(I):
    c = 1.5659e-2
    a1 = 0.6113
    a2 = 0.5146
    a3 = -0.3907
    return c + a1*I + a2*I**2 + a3*I**3   

B =[]
for i in I:
    b=BFeld(i)
    B.append(b)    
B=np.array(B)

#B2 =[]
#for i in I2:
#    b=BFeld(i)
#    B2.append(b)    
#B2=np.array(B2)

#___________________Fehlerrechung________________________________
 
 
"""Ableitungen"""
def dmdalpha(alpha,a,k,T,epsilon,l,L):
    return -2*a*k*T/(epsilon*l*L*(1-l/(2*L)))*1/alpha**2

def dmda(alpha,a,k,T,epsilon,l,L):
    return 2*k*T/(epsilon*l*L*(1-l/(2*L))*alpha)

def dmdT(alpha,a,k,T,epsilon,l,L):
    return 2*a*k/(epsilon*l*L*(1-l/(2*L))*alpha)

def dmdepsilon(alpha,a,k,T,epsilon,l,L):
    return -2*a*k*T/(epsilon**2*l*L*(1-l/(2*L))*alpha)

def dmdl(alpha,a,k,T,epsilon,l,L):
    return 8*a*k*T*(l-L)/(epsilon*l**2*(2*L-l)**2*alpha)

def dmdL(alpha,a,k,T,epsilon,l,L):
    return -8*a*k*T/(alpha*epsilon*l*(2*L-l)**2)

def dBdc():
    return  1

def dBda1(I):
    return I

def dBda2(I):
    return I**2
    
def dBda3(I):
    return I**3
    
def dBdI(a1,a2,a3,I):
    return a1 + 2*a2*I + 3*a3*I**2
    

"""Fehler auf m"""

def um(alpha,a,k,T,epsilon,l,L,err_alpha,err_a,err_T,err_epsilon,err_l,err_L):
    dalpha = dmdalpha(alpha,a,k,T,epsilon,l,L)
    da = dmda(alpha,a,k,T,epsilon,l,L)
    dT = dmdT(alpha,a,k,T,epsilon,l,L)
    depsilon = dmdepsilon(alpha,a,k,T,epsilon,l,L)
    dl = dmdl(alpha,a,k,T,epsilon,l,L)
    dL = dmdL(alpha,a,k,T,epsilon,l,L)
    return np.sqrt((dalpha*err_alpha)**2 + (da*err_a)**2 + (dT*err_T)**2 + ( depsilon*err_epsilon)**2 + (dl*err_l)**2 + (dL*err_L)**2)

"""Fehler auf B"""

def uB (c,a1,a2,a3,I,err_c, err_a1, err_a2, err_a3, err_I):
    dc = dBdc()
    da1 = dBda1(I)
    da2 = dBda2(I)
    da3 = dBda3(I)
    dI = dBdI(a1,a2,a3,I)
    return np.sqrt((dc*err_c)**2 + (da1 * err_a1)**2 + (da2 * err_a2)**2 + (da3 * err_a3)**2 + (dI * err_I)**2)


#_________________________Konstanten_______________________
epsilon = 0.953
err_epsilon = 0.0026
L = 7*10**(-2)
l = 0.455
a = 2.5 * 10**-(3)
k = 1.381 * 10**(-23)
T = np.mean(Tlist)

c = 1.5659e-2
a1 = 0.6113
a2 = 0.5146
a3 = -0.3907



#__________________________Unsicherheiten_________________
err_L = 0.1e-3
err_l = 2e-3
err_T = np.std(Tlist)
err_epsilon = 0.0026

err_a = 0.1e-3
err_I = 0

err_c = 2.7819e-3
err_a1 = 2.0927e-2
err_a2 = 4.1541e-2
err_a3 = 2.2721e-2


#__________________________Fit,Plot_________________________
err_B = []
for i in I:
    ub = uB(c,a1,a2,a3,i,err_c, err_a1, err_a2, err_a3, err_I)
    err_B.append(ub)
err_B = np.array(err_B)



def f(x, alpha, b):
    return x*alpha + b

fitparam, cov = curve_fit(f, q, B, sigma = err_B , p0 = [0.00808425613302,-0.00034293204896])
alpha, b = fitparam

err_alpha = np.sqrt(cov[0:1,0:1])

#alpha,b = np.polyfit(B, q, 1)           #alpha = Steigung, b = y-Achsenabschnitt
#m2,b2 = np.polyfit(B2, q2, 1)



plt.figure()
plt.plot(q,alpha*q+b)
plt.errorbar(q,B,yerr=err_B,  fmt='x')
#plt.plot(B2,m2*B2+b2)
plt.ylabel("Magnet Feld")
plt.xlabel("q")
#plt.savefig("Fit", dpi=300)
plt.show()





m = a*k*T*2/(alpha*epsilon*l*L*(1-L/(2*l))) 
um = um(alpha,a,k,T,epsilon,l,L,err_alpha,err_a,err_T,err_epsilon,err_l,err_L)
print(m, um)           
