import json

def tulosta_henkilot(tiedosto: str):
    try:
        with open(tiedosto, 'r') as tiedosto_avaus:
            data = json.load(tiedosto_avaus)

        for henkilo in data:
            nimi = henkilo["nimi"]
            ika = henkilo["ika"]
            harrastukset = ", ".join(henkilo["harrastukset"])
            print(f"{nimi} {ika} vuotta ({harrastukset})")

    except FileNotFoundError:
        print(f"Tiedostoa {tiedosto} ei löytynyt.")
    except json.JSONDecodeError:
        print(f"Virhe JSON-tiedoston lukemisessa.")


tiedosto = "opiskelijat.json"
tulosta_henkilot(tiedosto)
