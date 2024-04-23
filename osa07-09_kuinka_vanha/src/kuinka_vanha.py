from datetime import datetime

def paivien_laskeminen(pvm1, pvm2):
    return (pvm1 - pvm2).days

def kuinka_vanha(paiva, kuukausi, vuosi):
    syntymapaiva = datetime(vuosi, kuukausi, paiva)
    vertailupaiva = datetime(1999, 12, 31)
    paivien_erotus = paivien_laskeminen(syntymapaiva, vertailupaiva)

    if syntymapaiva > vertailupaiva:
        print(f"Et ollut syntynyt kun vuosituhat vaihtui.")
    else:
        print(f"Olit {paivien_erotus} päivää vanha kun vuosituhat vaihtui.")

if __name__ == "__main__":
    paiva = int(input("Päivä: "))
    kuukausi = int(input("Kuukausi: "))
    vuosi = int(input("Vuosi: "))

    kuinka_vanha(paiva, kuukausi, vuosi)

