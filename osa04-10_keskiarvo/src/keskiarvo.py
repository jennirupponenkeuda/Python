# tee ratkaisu tänne
def keskiarvo(luvut):
    if not luvut:
        return None

    summa = sum(luvut)
    keskiarvo = summa / len(luvut)
    return keskiarvo

# Lisätään if __name__ == "__main__": -rakenne
if __name__ == "__main__":
    # Esimerkki käytöstä
    lista = [1, 2, 3]
    vastaus = keskiarvo(lista)
    print("vastaus:", vastaus)
