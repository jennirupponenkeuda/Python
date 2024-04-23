import random

def sanat(maara: int, alku: str):
    try:
        with open("sanat.txt", "r", encoding="utf-8") as tiedosto:
            sanalista = [rivi.strip() for rivi in tiedosto.readlines() if rivi.startswith(alku)]

            if len(sanalista) < maara:
                raise ValueError("Ei tarpeeksi sanoja annetulla alulla")

            satunnaiset_sanat = random.sample(sanalista, maara)
            return satunnaiset_sanat

    except FileNotFoundError:
        print("Tiedostoa 'sanat.txt' ei löytynyt.")
        return None
    except ValueError as ve:
        print(f"Virhe: {ve}")
        return None
    except Exception as e:
        print(f"Muukalainen virhe: {e}")
        return None

if __name__ == "__main__":
    lista = sanat(3, "ca")
    if lista is not None:
        for sana in lista:
            print(sana)

