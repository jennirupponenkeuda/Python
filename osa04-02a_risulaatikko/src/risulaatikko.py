# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva (leveys, merkkijono):
    if not merkkijono:
        merkkijono = "*"
    print(merkkijono[0] * leveys)

def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    for i in range(korkeus):
        if korkeus == 0 or i == korkeus -1:
            viiva(10, "#")
        else:
            viiva(10, "#        #")


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)
