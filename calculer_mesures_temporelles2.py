import numpy as np
mesures={}


def calculer_mesures_temporelles(liste_RR, difference_RR, difference_carre_RR,nb_pts,liste_pic):


    bpm = len(liste_pic)
    sdnn = np.std(liste_RR) #variabilite globale
    variance = np.var(liste_RR)
    ibi = np.mean(liste_RR)
    sdsd = np.std(difference_RR)
    rmssd = np.sqrt(np.mean(difference_carre_RR))
    nn50 = [x for x in difference_RR if (x > 50)]
    if nn50:
        pnn50 = float(len(nn50)) / float(len(difference_RR))

    return sdnn, variance, ibi, sdsd, rmssd, nn50, bpm
