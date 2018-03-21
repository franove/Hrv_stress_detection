import fenetre_glissante_BSV as fen
import csv


def ajouter_ligne_data_bsv():
    
    with open('data_general_hrv/data_bsv.csv', 'a') as csvfile:
                    fwriter = csv.writer(csvfile, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
                    fwriter.writerow(fen.mesures['BSVL'])

    with open('data_general_hrv/data_sdnn.csv', 'a') as csvfile:
                    fwriter = csv.writer(csvfile, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
                    fwriter.writerow(fen.mesures['sdnn'])

    with open('data_general_hrv/data_variance.csv', 'a') as csvfile:
        fwriter = csv.writer(csvfile, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
        fwriter.writerow(fen.mesures['variance'])
                    
    with open('data_general_hrv/data_ibi.csv', 'a') as csvfile:
                    fwriter = csv.writer(csvfile, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
                    fwriter.writerow(fen.mesures['ibi'])

    with open('data_general_hrv/data_sdsd.csv', 'a') as csvfile:
                    fwriter = csv.writer(csvfile, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
                    fwriter.writerow(fen.mesures['sdsd'])
                    
    with open('data_general_hrv/data_rmssd.csv', 'a') as csvfile:
                    fwriter = csv.writer(csvfile, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
                    fwriter.writerow(fen.mesures['rmssd'])