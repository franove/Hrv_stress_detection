import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d 
import seuillage as s 
import calculer_RR2 as rr
import detecter_pic as detect

mesures={}


def tracer_RR():
    liste_pic = detect.mesures['liste_pic']
    liste_RR = rr.mesures['liste_RR']
    x_RR = liste_pic[1:]
    y_RR = liste_RR
    plt.figure(1)
    plt.subplot(3, 1, 2)
    plt.plot(x_RR, y_RR, label="Original", color='blue')
    RR_x = np.linspace(x_RR[0],x_RR[-1],x_RR[-1]) 
    f = interp1d(x_RR, y_RR,  kind='cubic') 
    plt.plot(RR_x, f(RR_x), label="Original", color='red')
    plt.axhline(y=s.mesures['seuil_inf'], color='yellow')
    plt.axhline(y=s.mesures['seuil_sup'], color='yellow')
    mesures['signal_interp']=f(RR_x)
   

