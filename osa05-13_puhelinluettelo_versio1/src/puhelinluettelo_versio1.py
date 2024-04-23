puhelinluettelo = {}

while True:
    komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")

    if komento == "1":
        nimi = input("nimi: ")
        if nimi in puhelinluettelo:
            print(puhelinluettelo[nimi])
        else:
            print("ei numeroa")

    elif komento == "2":
        nimi = input("nimi: ")
        numero = input("numero: ")
        puhelinluettelo[nimi] = numero
        print("ok!")

    elif komento == "3":
        print("lopetetaan...")
        break

    else:
        print("Virheellinen komento. Yritä uudelleen.")
