import matplotlib.pyplot as plt
import numpy as np
import Echantillonnage_filtrage as ech
mesures={}

##########################################################################################    

##########################################################################################


def transformee_fourier(signal):
    f = ech.mesures['f']
    n = len(signal)  # Longueur signal
    frq = np.fft.fftfreq(len(signal), d=(1./f))
    frq = frq[range(n//2)]
    Y = np.fft.fft(signal)/n  # On divise par la taille du vecteur pour normaliser la fft
    Y = Y[range(n//2)]

    # plt.subplot(3, 1, 3)
    # plt.xlim(0, 0.6)
    # plt.ylim(0, 50)
    # plt.xlim(0, 0.6)
    # plt.ylim(0, 50)
    #
    # plt.plot(frq, abs(Y), color="blue")
    # plt.show()
    plt.title("Analyse frequentielle")
    mesures['fourier'] = Y
    mesures['frq'] = frq
   

##########################################################################################

########################################################################################## 
