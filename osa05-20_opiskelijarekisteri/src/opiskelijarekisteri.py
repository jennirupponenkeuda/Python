def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = []

def tulosta(opiskelijat: dict, nimi: str):
    if nimi in opiskelijat:
        print(f"{nimi}:")
        suoritukset = opiskelijat[nimi]
        if not suoritukset:
            print(" ei suorituksia")
        else:
            for suoritus in suoritukset:
                print(f" {suoritus[0]} {suoritus[1]}")
            keskiarvo = sum(arvosana for _, arvosana in suoritukset) / len(suoritukset)
            print(f" keskiarvo {keskiarvo:.2f}")
    else:
        print(f"ei löytynyt ketään nimellä {nimi}")

def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
    if nimi in opiskelijat:
        kurssi, arvosana = suoritus
        for i, s in enumerate(opiskelijat[nimi]):
            if s[0] == kurssi:
                # Jos uusi arvosana on suurempi kuin vanha, päivitä arvosana
                if arvosana > s[1]:
                    opiskelijat[nimi][i] = (kurssi, arvosana)
                break
        else:
            opiskelijat[nimi].append(suoritus)

def kooste(opiskelijat: dict):
    if not opiskelijat:
        print("Ei opiskelijoita.")
        return

    eniten_suorituksia = max(opiskelijat, key=lambda n: len(opiskelijat[n]))
    paras_keskiarvo = max(opiskelijat, key=lambda n: sum(s[1] for s in opiskelijat[n]) / len(opiskelijat[n]))

    print(f"opiskelijoita {len(opiskelijat)}")
    print(f"eniten suorituksia {len(opiskelijat[eniten_suorituksia])} {eniten_suorituksia}")
    paras_opiskelija = max(opiskelijat, key=lambda n: sum(s[1] for s in opiskelijat[n]) / len(opiskelijat[n]))
    paras_keskiarvo = sum(s[1] for s in opiskelijat[paras_opiskelija]) / len(opiskelijat[paras_opiskelija])
    print(f"paras keskiarvo {paras_keskiarvo}")

if __name__ == "__main__":
    # Testataan
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    tulosta(opiskelijat, "Pekka")
    tulosta(opiskelijat, "Liisa")
    tulosta(opiskelijat, "Jukka")

    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    tulosta(opiskelijat, "Pekka")

    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 0))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 2))
    tulosta(opiskelijat, "Pekka")

    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 3))
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 0))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 2))
    lisaa_suoritus(opiskelijat, "Pekka", ("Jtkt", 1))
    tulosta(opiskelijat, "Liisa")
    tulosta(opiskelijat, "Pekka")

    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 0))
    tulosta(opiskelijat, "Pekka")

    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    tulosta(opiskelijat, "Pekka")

    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 5))
    tulosta(opiskelijat, "Pekka")

    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "emilia")
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_suoritus(opiskelijat, "emilia", ("Ohpe", 4))
    lisaa_suoritus(opiskelijat, "emilia", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "pekka", ("Tira", 3))
    lisaa_suoritus(opiskelijat, "pekka", ("Lama", 0))
    lisaa_suoritus(opiskelijat, "pekka", ("Tira", 2))
    lisaa_suoritus(opiskelijat, "pekka", ("Jtkt", 1))

    kooste(opiskelijat)

