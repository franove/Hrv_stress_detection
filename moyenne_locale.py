import pandas as pd
import math
import numpy as np
import Echantillonnage_filtrage as ech

##########################################################################################    

##########################################################################################

def moyenne_locale(ecg_data, hrw, coef_moyenne):
   
    f = ech.mesures['f']
    # my=pd.DataFrame(ecg_data.signal_filtre)
    # moyenne_glissante = my.rolling(hrw*f)
    moyenne_glissante = pd.rolling_mean(ecg_data.signal_filtre, hrw*f)
    moyenne_ecg = np.mean(ecg_data.battement)
    moyenne_glissante = [moyenne_ecg if math.isnan(x) else x for x in moyenne_glissante]
    moyenne_glissante = [coef_moyenne*x for x in moyenne_glissante]
    ecg_data['battement_moyenne'] = moyenne_glissante
    
##########################################################################################    

##########################################################################################
