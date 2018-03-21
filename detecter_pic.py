import calculer_RR2 as rr
mesures={}
##########################################################################################    

##########################################################################################
def detecter_pic(ecg_data):
    position_liste=0 
    fenetre_glissante=[]
    liste_pic=[]
    valeur_pic=[]
    for valeur in ecg_data.signal_filtre:
        moyenne_locale=ecg_data.battement_moyenne[position_liste]
      
        if valeur>moyenne_locale:
            fenetre_glissante.append(valeur)
            position_liste+=1
            
        elif (valeur <= moyenne_locale) and (len(fenetre_glissante)<=1):
          position_liste+=1
        else :
            position_liste+=1
            if fenetre_glissante:
                maximum_local=max(fenetre_glissante)
                position_maximum=position_liste-len(fenetre_glissante) + (fenetre_glissante.index(max(fenetre_glissante)))
                fenetre_glissante=[]
                liste_pic.append(position_maximum)
                valeur_pic.append(maximum_local)
            else:
                position_liste+=1
                
    mesures['liste_pic']=liste_pic
    mesures['valeur_pic']=valeur_pic
    print(liste_pic)

##########################################################################################    

##########################################################################################
