# Kirjoita ratkaisu tähän
luku1 = int(input("Luku 1:"))
luku2 = int(input("Luku 2:"))

summa = luku1 + luku2
tulo = luku1 * luku2
erotus = luku1 - luku2

komento = str(input("Komento:"))
if komento == str("summa"):
    print(f"{luku1} + {luku2} = {summa}")
if komento == str("tulo"):
    print(f"{luku1} * {luku2} = {tulo}")
if komento == str("erotus"):
    print(f"{luku1} - {luku2} = {erotus}")
    
