import Echantillonnage_filtrage as ech
import moyenne_locale as my
import detecter_pic as detect
import calculer_RR2 as rr
import calculer_mesures_temporelles2 as temp
import tracer_RR 
import seuillage as s 
import correction_RR
import afficher as aff
import fenetre_glissante_BSV as fg
import ajouter_data_bsv as add

ecg_data = ech.charger_data("/home/fsz/Bureau/Projet/data_processing/test/data_antoine_protocole.csv")
ech.executer_filtrage(ecg_data)
nb_pts = ech.calculer_nb_pts_fenetre()
my.moyenne_locale(ecg_data, 2, 1)  # data/fenetre/frequence/coef ajustement moyenne
detect.detecter_pic(ecg_data)
rr.calculer_rr(detect.mesures['liste_pic'])
rr.calculer_rr_diff(rr.mesures['liste_RR'])
temp.calculer_mesures_temporelles(rr.mesures['liste_RR'], rr.mesures['difference_RR'],
                                   rr.mesures['difference_carre_RR'],5002,detect.mesures['liste_pic'])
s.seuillage()
tracer_RR.tracer_RR()
correction_RR.correction_RR()
fg.fenetre_glissante_bsv(5002)  # Calcul temporel et fréquentiel dans une fenêtre de n points
aff.afficher_signal(ecg_data, "Electrocardiogramme")
aff.afficher_grandeur_hrv()
add.ajouter_ligne_data_bsv()
