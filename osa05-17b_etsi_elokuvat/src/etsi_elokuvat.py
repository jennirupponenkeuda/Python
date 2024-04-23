def etsi_elokuvat(rekisteri: list, hakusana: str):
    hakusana_lower = hakusana.lower()  # Muunnetaan hakusana pieniksi kirjaimiksi
    loydetyt_elokuvat = []

    for elokuva in rekisteri:
        nimi_lower = elokuva["nimi"].lower()  # Muunnetaan elokuvan nimi pieniksi kirjaimiksi
        if hakusana_lower in nimi_lower:
            loydetyt_elokuvat.append(elokuva)

    return loydetyt_elokuvat

if __name__ == "__main__":
    rekisteri = [
        {"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
        {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
        {"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}
    ]

    hakusana = input("Anna hakusana: ")
    loydetyt_elokuvat = etsi_elokuvat(rekisteri, hakusana)

    if loydetyt_elokuvat:
        print("Löydetyt elokuvat:")
        for elokuva in loydetyt_elokuvat:
            print(elokuva)
    else:
        print("Elokuvia ei löytynyt.")
