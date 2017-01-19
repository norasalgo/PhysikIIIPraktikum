# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:40:34 2017

@author: Nora
"""

import numpy as np
import matplotlib.pyplot as plt
from excelreadSternGerlach import machliste



#____________________Messdaten_______________________________

serie = 2

if serie == 1:          #Set1 mit Ausreisser
    q = np.array([5.6536, 5.8741, 4.4131, 3.7338, 2.4297, 1.8257])*10**(-3)
    err_q = np.array([0.0349, 0.0343, 0.0268, 0.0217, 0.0137, 0.0103])*10**(-3)

    I = np.array([1000.0, 900.0, 800.0, 700.0, 500.0, 403.0])*10**(-3)
    T = np.array([186.4, 185.0, 185.2, 185.6, 185.8, 185.9])+273

    I2 = np.array([1000.0, 800.0, 700.0, 500.0, 403.0])*10**(-3)
    q2 = np.array([5.6536, 4.4131, 3.7338, 2.4297, 1.8257])*10**(-3)

elif serie == 2:        #Set 2, viel schöner :)
    q = np.array([5.7280,5.3001,4.7840,4.2071,3.5424,2.2464])*10**(-3)
    err_q = np.array([0.0041,0.0032,0.0032,0.0029,0.0025,0.0015])*10**(-3)
    
    I = np.array([1000,900,800,700,600,402])*10**(-3)
    T = np.array([187.5,186.7,186.5,186.5,186.3,184.1])+273
 
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


#__________________________Fit__________________________

alpha,b = np.polyfit(B, q, 1)           #alpha = Steigung, b = y-Achsenabschnitt
#m2,b2 = np.polyfit(B2, q2, 1)


#__________________________Plot_________________________
plt.figure()
plt.plot(B,alpha*B+b)
plt.errorbar(B,q,yerr=err_q,  fmt='x')
#plt.plot(B2,m2*B2+b2)
plt.xlabel("Magnet Feld")
plt.ylabel("q")
plt.show()

#_________________________Konstanten_______________________
epsilon = 0.953
err_epsilon = 0.0026
L = 7*10**(-2)
l = 0.455
a = 2.5 * 10**-(3)
k = 1.381 * 10**(-23)

#___________________________Fehlerrechnung
err_L = 0.1e-3
err_l = 2e-3
err_T = np.std(T)
err_epsilon = 0.0026
err_alpha = 0
err_a = 0.1e-3


m = alpha*a*k*T*2/(epsilon*l*L*(1-L/(2*l))) 

print(m)           
