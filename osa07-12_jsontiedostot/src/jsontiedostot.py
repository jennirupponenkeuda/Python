# tee ratkaisu tänne
import json

def tulosta_henkilot(tiedosto: str):
    with open(tiedosto, 'r') as json_tiedosto:
        data = json_tiedosto.read()
        henkilot = json.loads(data)

        for henkilo in henkilot:
            nimi = henkilo.get("nimi", "")
            ika = henkilo.get("ika", "")
            harrastukset = ", ".join(henkilo.get("harrastukset", []))

            print(f"{nimi} {ika} vuotta ({harrastukset})")

if __name__ == "__main__":
    tulosta_henkilot('henkilot.json')
