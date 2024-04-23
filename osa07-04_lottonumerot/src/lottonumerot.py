# tee ratkaisu tänne
from random import sample

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    if maara > ylaraja - alaraja + 1:
        raise ValueError("Määrä ei voi olla suurempi kuin lukualueen pituus.")
    
    kaikki_numerot = list(range(alaraja, ylaraja + 1))

    lista_lottonumeroista = sample(kaikki_numerot, maara)

    return sorted(lista_lottonumeroista)


if __name__ == "__main__":
    for numero in lottonumerot(7, 1, 40):
        print(numero)
