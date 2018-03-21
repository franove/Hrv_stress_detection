import tracer_RR as tr
import fourier as fft
import calcul_bsv as bsv
import ajouter_data_bsv as liste_bsv

import matplotlib.pyplot as plt
import numpy as np
import detecter_pic as detect
import calculer_RR2 as rr
import calculer_mesures_temporelles2 as temp
import Echantillonnage_filtrage as freq
mesures ={}

def fenetre_glissante_bsv(nb_pts):
    
    BSVL = []
    signal= []
    liste_abs = []
    signal_interp = tr.mesures['signal_interp']
    x = 0
    pics = detect.mesures['liste_pic']

    liste_sdnn = []
    liste_variance = []
    liste_ibi = []
    liste_sdsd = []
    liste_rmssd = []
    liste_nn50 = []
    liste_bpm = []

    while x < len(signal_interp):

        signal = signal_interp[x:x+nb_pts]
        print(len(signal))
        transformee_fourier = fft.transformee_fourier(signal)
        BSV = bsv.balance_sv(transformee_fourier)
        BSVL.append(BSV)
        liste_pic = []

        for valeur in pics:
            if valeur >= x and valeur <= x+nb_pts:      # On recupere la position des pics dans notre fenetre glissante
                liste_pic.append(valeur)

        liste_rr = rr.calculer_rr(liste_pic)
        diff_rr, diff_rr_carre = rr.calculer_rr_diff(liste_rr)

        print("liste_pic:", liste_pic)
        print("liste_rr:", liste_rr)
        print("difference RR successif : ", diff_rr)
        print("difference_RR_carré:", diff_rr_carre)


        sdnn, variance, ibi, sdsd, rmssd, nn50, bpm = temp.calculer_mesures_temporelles(liste_rr, diff_rr, diff_rr_carre, nb_pts,liste_pic)
        liste_sdnn.append(sdnn), liste_variance.append(variance), liste_ibi.append(ibi),
        liste_sdsd.append(sdsd), liste_rmssd.append(rmssd), liste_nn50.append(nn50), liste_abs.append((x+nb_pts/2)/6000), liste_bpm.append(bpm)

        # i = 0
        # if x >= 11004 and x <= 16006:
        #
        #     i += 1
        #     somme += x
        #
        # elif x >= 16006 and x <= 21008:
        #
        #     i += 1
        #     somme += x


        x += int(freq.mesures['f'])  # freq.mesures['f']

    fourier_signal_total = fft.transformee_fourier(signal_interp)
    print("Balance sympatho-vagale",BSVL)
    BSV_signal_total = bsv.balance_sv(fourier_signal_total)
    #BSVL.append(BSV_signal_total)


    print("Balance sympatho-vagale sur tout le signal", BSV_signal_total)

    mesures['sdnn'] = liste_sdnn
    mesures['variance'] = liste_variance
    mesures['ibi'] = liste_ibi
    mesures['sdsd'] = liste_sdsd
    mesures['rmssd'] = liste_rmssd
    mesures['nn50'] = liste_nn50
    mesures['BSVL'] = BSVL
    mesures['abscisse'] = liste_abs
    mesures['bpm'] = liste_bpm
    # plt.figure(1)
    # plt.subplot(3,1,3)
    # plt.xlim(0, 40)
    # plt.ylim(0, 45)
    # y = range(0, len(BSVL))
    # plt.scatter(y, BSVL)
    # plt.plot(BSVL)
    # # plt.show()
    # y = range(0, len(liste_rmssd))
    # plt.scatter(y, liste_rmssd)
    # plt.plot(liste_rmssd)
    # plt.show()
    print(np.std(BSVL))