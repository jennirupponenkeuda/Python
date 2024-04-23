def oikeinkirjoitustarkistus(teksti, sanalista):
    sanat = teksti.split()
    korjattu_teksti = ""

    for sana in sanat:
        korjattu_sana = sana
        if sana.lower() not in sanalista:
            korjattu_sana = f"*{sana}*"

        korjattu_teksti += korjattu_sana + " "

    return korjattu_teksti.strip()

def lue_sanalista(tiedostonimi):
    try:
        with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
            sanalista = set(sana.strip().lower() for sana in tiedosto.readlines())
        return sanalista
    except FileNotFoundError:
        print(f"Virhe: Tiedostoa {tiedostonimi} ei löydy.")
        return set()




