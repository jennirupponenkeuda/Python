# tee ratkaisu tänne
import string

def jaa_merkkeihin(merkkijono: str):
    kirjaimet = string.ascii_letters
    valimerkit = string.punctuation

    kirjainjono = ""
    valimerkitjono = ""
    muutjono= ""

    for merkki in merkkijono:
        if merkki in kirjaimet:
            kirjainjono += merkki
        elif merkki in valimerkit:
            valimerkitjono += merkki
        else:
            muutjono += merkki
    return (kirjainjono, valimerkitjono,muutjono)
