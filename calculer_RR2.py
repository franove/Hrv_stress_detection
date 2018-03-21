import math
import Echantillonnage_filtrage as ech

import detecter_pic as detect

mesures = {}
##########################################################################################    

##########################################################################################


def calculer_rr(liste_pic):
    f = ech.mesures['f']
    liste_RR=[]

    i=0
    while i < len(liste_pic)-1:
        intervalle_RR=liste_pic[i+1]-liste_pic[i]
        RR_ms = (1000*intervalle_RR)/f
        liste_RR.append(RR_ms)
        i += 1

    mesures['liste_RR'] = liste_RR
    return liste_RR


def calculer_rr_diff(liste_RR):
    difference_RR = []
    difference_carre_RR = []
    liste_RR = mesures['liste_RR']

    j = 0
    while j < len(liste_RR)-1:
        difference_RR.append(abs(liste_RR[j]-liste_RR[j+1]))
        difference_carre_RR.append(math.pow(liste_RR[j] - liste_RR[j+1], 2))
        j += 1
    mesures['difference_RR']=difference_RR
    mesures['difference_carre_RR']=difference_carre_RR
    return difference_RR,difference_carre_RR
##########################################################################################    

##########################################################################################
