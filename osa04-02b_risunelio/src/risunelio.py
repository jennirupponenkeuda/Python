def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)

def risulaatikko(korkeus, leveys, merkki):
    i = 0
    while i < korkeus:
        viiva(leveys, merkki)
        i += 1

def risunelio(koko):
    i = 0
    while i < koko:
        risulaatikko(koko, koko, "#")
        i += 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
