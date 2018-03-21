import pandas as pd

from scipy.signal import butter, lfilter

mesures = {}


def charger_data(fichier):
    
    ecg_data = pd.read_csv(fichier)
    ecg_data = ecg_data[100:120000].reset_index(drop=True)
    return ecg_data



def calcul_ech(ecg_data):
    echantillonnage = [x for x in ecg_data.time]
    mesures['f'] = (1000*len(echantillonnage)/(echantillonnage[-1]-echantillonnage[0]))
  
    mesures['duree'] = echantillonnage[-1]-echantillonnage[0]


def calculer_nb_pts_fenetre():

    duree = mesures['duree']
    print("duree total :", duree,"ms")
    nb_pts = duree*mesures['f']/6000  # On veut 6 segments de une min environ -> protocole
    print("nombre de point dans une minute :", nb_pts)


def butter_passe_bas( f_coupure, f,  ordre=5):
    f = mesures['f']
    nyq = 0.5 * f
    normalCutoff =  f_coupure / nyq
    b, a = butter(ordre, normalCutoff, btype='low', analog = False)
    
    return b, a


def butter_filtre_passe_bas(ecg_data, f_coupure, f, ordre=5):
    f=mesures['f']
    b, a = butter_passe_bas( f_coupure, f, ordre=ordre)
    y = lfilter(b, a, ecg_data)
    return y


def filtrer(ecg_data):
    f = mesures['f']
    signal_filtre= butter_filtre_passe_bas(ecg_data.battement, 2.5, f, 5)#filter the signal with a cutoff at 2.5Hz and a 5th order Butterworth filter
    ecg_data['signal_filtre']=signal_filtre
    mesures['ecg_data']=signal_filtre



def executer_filtrage(ecg_data):
    calcul_ech(ecg_data)
    filtrer(ecg_data)
