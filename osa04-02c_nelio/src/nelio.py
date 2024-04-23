# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)

def risulaatikko(leveys, merkki):
    viiva(leveys, merkki)

def viiva(koko, merkki):
    if merkki == "":
        merkki = "*"
    print(merkki[0] * koko)

def risulaatikko(leveys, merkki):
    viiva(leveys, merkki)

def risunelio(koko):
    i = 0
    while i < koko:
        risulaatikko(koko, "#")
        i += 1

def nelio(koko, merkki):
    i = 0
    while i < koko:
        risulaatikko(koko, merkki)
        i += 1

