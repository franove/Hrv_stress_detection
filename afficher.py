import matplotlib.pyplot as plt
import detecter_pic as pic
import correction_RR as crr
import calculer_mesures_temporelles2 as cmt
import fenetre_glissante_BSV as fen


def afficher_signal(ecg_data, titre):
  
    liste_pic = pic.mesures['liste_pic']
    valeur_pic = pic.mesures['valeur_pic']

    plt.figure(1)
    plt.subplot(3, 1, 1)
    plt.title(titre) 
    x_lim = 1.2*liste_pic[-1]
    plt.xlim(0, x_lim)

    plt.plot(ecg_data.battement_moyenne, color='green')
    plt.plot(ecg_data.signal_filtre, color='black', alpha=0.5)
    plt.scatter(liste_pic, valeur_pic, color='yellow' )
    plt.scatter(crr.mesures['x_battement_suspect'], crr.mesures['y_battement_suspect'], color='red', label="Pic incertain")
    plt.legend(loc=4, framealpha=0.9)
    plt.show()
    
def afficher_grandeur_hrv():
    plt.figure(2)

    plt.subplot(6, 1, 1)
    plt.title("sdnn")
    plt.plot(fen.mesures['abscisse'],fen.mesures['sdnn'])
    plt.tight_layout(pad=1.8, w_pad=0.5, h_pad=2.0)

    plt.subplot(6, 1, 2)
    plt.title("variance")
    plt.plot(fen.mesures['abscisse'], fen.mesures['variance'])

    plt.subplot(6, 1, 3)
    plt.title("ibi")
    plt.plot(fen.mesures['abscisse'], fen.mesures['ibi'])

    plt.subplot(6, 1, 4)
    plt.title("sdsd")
    plt.plot(fen.mesures['abscisse'], fen.mesures['sdsd'])

    plt.subplot(6, 1, 6)
    plt.title("rmssd")
    plt.plot(fen.mesures['abscisse'], fen.mesures['rmssd'])
    #
    # plt.subplot(6, 1, 5)
    # plt.title("Balance sympatho-vagale")
    # plt.ylim(0, 3)
    # plt.plot(fen.mesures['abscisse'],fen.mesures['BSVL'])

    plt.subplot(6, 1, 5)
    plt.title("bpm")
    plt.ylim(70,90)
    plt.plot(fen.mesures['abscisse'],fen.mesures['bpm'])

    plt.show()
