from datetime import datetime, timedelta

def huijarit(tentti_tiedosto, palautus_tiedosto):
    def parse_aika(aika_str):
        return datetime.strptime(aika_str, "%H:%M")

    huijarit_lista = set()

    # Lue tenttien aloitusajat
    with open(tentti_tiedosto, 'r') as tiedosto:
        tentti_ajat = {}
        for rivi in tiedosto:
            tunnus, aika_str = rivi.strip().split(";")
            tentti_ajat[tunnus] = parse_aika(aika_str)

    # Tarkista palautusajat
    with open(palautus_tiedosto, 'r') as tiedosto:
        for rivi in tiedosto:
            tunnus, _, _, palautus_aika_str = rivi.strip().split(";")
            palautus_aika = parse_aika(palautus_aika_str)

            # Etsi opiskelijat, jotka ovat käyttäneet yli 3 tuntia
            if (palautus_aika - tentti_ajat[tunnus]) > timedelta(hours=3):
                huijarit_lista.add(tunnus)

    return list(huijarit_lista)

