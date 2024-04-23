def lisaa_merkinta(paivakirja_tiedosto):
    merkinta = input("Anna merkintä: ")
    with open(paivakirja_tiedosto, "a", encoding="utf-8") as tiedosto:
        tiedosto.write(merkinta + "\n")
    print("Päiväkirja tallennettu")

def lue_merkinnat(paivakirja_tiedosto):
    try:
        with open(paivakirja_tiedosto, "r", encoding="utf-8") as tiedosto:
            merkinnat = tiedosto.readlines()
        if not merkinnat:
            print("Päiväkirja on tyhjä.")
        else:
            print("Merkinnät:")
            for merkinta in merkinnat:
                print(merkinta.strip())
    except FileNotFoundError:
        print("Päiväkirjatiedostoa ei löydy. Aloita uusi päiväkirja.")


paivakirja_tiedosto = "paivakirja.txt"

while True:
    print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    valinta = input("Valinta: ")

    if valinta == "1":
        lisaa_merkinta(paivakirja_tiedosto)
    elif valinta == "2":
        lue_merkinnat(paivakirja_tiedosto)
    elif valinta == "0":
        print("Heippa!")
        break
    else:
        print("Virheellinen valinta. Yritä uudelleen.")




