# tee ratkaisu tänne
def summa(lista1: list, lista2: list) -> list:
    tulos = []
    for i in range(len(lista1)):
        summa = lista1[i] + lista2[i]
        tulos.append(summa)
    return tulos


