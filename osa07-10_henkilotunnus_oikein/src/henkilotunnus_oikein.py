from datetime import datetime, timedelta
def onko_validi(paivamaara):
    try:
        datetime.strptime(paivamaara, "%d%m%y")
        return True
    except ValueError:
        return False

def tallenna_ruutuajat(tiedoston_nimi, aloituspäivä, päivien_määrä):
    tiedosto = open(tiedoston_nimi, "w")
    tiedosto.write(f"Ajanjakso: {aloituspäivä} - {aloituspäivä + timedelta(days=päivien_määrä-1)}\n")
    
    yhteensä_minuutteja = 0
    keskiarvo_minuutteja = 0

    for päivä in range(päivien_määrä):
        ruutuajat = input(f"Ruutuaika {aloituspäivä + timedelta(days=päivä)} (TV tietokone mobiililaite): ").split()
        ruutuajat = [int(minuutit) for minuutit in ruutuajat]
        
        yhteensä_minuutteja += sum(ruutuajat)
        keskiarvo_minuutteja = yhteensä_minuutteja / (päivä + 1)
        
        tiedosto.write(f"{aloituspäivä + timedelta(days=päivä)}: {'/'.join(map(str, ruutuajat))}\n")

    tiedosto.write(f"Yht. minuutteja: {yhteensä_minuutteja}\n")
    tiedosto.write(f"Keskim. minuutteja: {keskiarvo_minuutteja}\n")
    
    tiedosto.close()
    print(f"Tiedot tallennettu tiedostoon {tiedoston_nimi}")

if __name__ == "__main__":
    tiedostonimi = input("Tiedosto: ")
    aloituspäivä = datetime.strptime(input("Aloituspäivä: "), "%d.%m.%Y")
    päivien_määrä = int(input("Montako päivää: "))

    tallenna_ruutuajat(tiedostonimi, aloituspäivä, päivien_määrä)
