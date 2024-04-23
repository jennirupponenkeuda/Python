def suurin():
    with open("luvut.txt") as tiedosto:
        luvut = [int(rivi.strip()) for rivi in tiedosto.readlines()]

    suurin_luku = max(luvut)
    return suurin_luku

if __name__ == "__main__":
    suurin_luku = suurin()
    print(suurin_luku)
