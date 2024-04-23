# tee ratkaisu tänne
import csv
def lue_hedelmat():
        hedelmat_sanakirja = {}

    
        with open ("hedelmat.csv", encoding='utf-8') as tiedosto:
            lukija = csv.reader(tiedosto, delimiter = ";")

            for rivi in lukija:
                hedelman_nimi = rivi[0]
                hedelman_hinta = float(rivi[1])
                hedelmat_sanakirja[hedelman_nimi] = hedelman_hinta
        
        return hedelmat_sanakirja

if __name__ == "__main__" :
    hedelmat_dict = lue_hedelmat()
    print(lue_hedelmat())

