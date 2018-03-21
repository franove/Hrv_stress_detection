import detecter_pic as pic
import calculer_RR2 as rr
import seuillage as s 
mesures={}
##########################################################################################    

##########################################################################################
def correction_RR():
  
    liste_RR=rr.mesures['liste_RR']
    seuil_sup =s.mesures['seuil_sup']
    seuil_inf = s.mesures['seuil_inf']
    liste_pic=pic.mesures['liste_pic']
    valeur_pic=pic.mesures['valeur_pic']
    
    x_battement_suspect=[]
    y_battement_suspect=[]
    liste_RR_corrigee=[]
    
    i=0
    while i<len(liste_RR):
        if (liste_RR[i]>seuil_inf) and (liste_RR[i]<seuil_sup):
            liste_RR_corrigee.append(liste_RR[i])
           
            i+=1
        else :
            x_battement_suspect.append(liste_pic[i+1])
            y_battement_suspect.append(valeur_pic[i+1])
            i+=1
    mesures['liste_RR_corrigee']=liste_RR_corrigee
    mesures['x_battement_suspect']=x_battement_suspect
    mesures['y_battement_suspect']=y_battement_suspect
         
###########################################################################################    

###########################################################################################
