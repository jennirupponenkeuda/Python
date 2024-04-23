# Kirjoita ratkaisu tähän
lista = [1,2,3,4,5]
while True:
    indeksi = int(input("Anna indeksi:"))

    if indeksi == -1:
        break

    if 0 <= indeksi < len(lista):
        arvo = int(input("Anna arvo:"))
        lista[indeksi] = arvo
        print(lista)
    else:
        break