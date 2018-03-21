import numpy as np
#import transformee_fourier_rapide as fft
import fourier as fft


def balance_sv(transformee_fourier):
    
    Y = fft.mesures['fourier']
    frq = fft.mesures['frq']
    lf = np.trapz(abs(Y[(frq >= 0.04) & (frq <= 0.15)]))
    hf = np.trapz(abs(Y[(frq >= 0.15) & (frq <= 0.4)]))
    balance_SV = lf/hf
    return balance_SV
