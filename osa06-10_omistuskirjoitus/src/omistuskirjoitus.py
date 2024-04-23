def luo_omistuskirjoitus():
    vastaanottaja = input("Kenelle teos omistetaan: ")
    tiedostonnimi = input("Mihin kirjoitetaan: ")

    with open(tiedostonnimi, "w", encoding='utf-8', errors='replace') as tiedosto:
        teksti = f"Hei {vastaanottaja}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi"
        tiedosto.write(teksti)


luo_omistuskirjoitus()

