# tee ratkaisu tänne
def kumpi_voitti(pelilauta):
    koko = len(pelilauta)

    def onko_piste_pelilaudalla(x, y):
        return 0 <= x < koko and 0 <= y < koko

    def tarkista_aluetta(x, y, pelaaja, alue):
        if onko_piste_pelilaudalla(x, y) and pelilauta[x][y] == pelaaja and (x, y) not in alue:
            alue.add((x, y))
            tarkista_aluetta(x + 1, y, pelaaja, alue)
            tarkista_aluetta(x - 1, y, pelaaja, alue)
            tarkista_aluetta(x, y + 1, pelaaja, alue)
            tarkista_aluetta(x, y - 1, pelaaja, alue)

    pelaaja1_alueet = set()
    pelaaja2_alueet = set()

    for i in range(koko):
        for j in range(koko):
            if pelilauta[i][j] == 1 and (i, j) not in pelaaja1_alueet:
                alue = set()
                tarkista_aluetta(i, j, 1, alue)
                pelaaja1_alueet.update(alue)
            elif pelilauta[i][j] == 2 and (i, j) not in pelaaja2_alueet:
                alue = set()
                tarkista_aluetta(i, j, 2, alue)
                pelaaja2_alueet.update(alue)

    if len(pelaaja1_alueet) > len(pelaaja2_alueet):
        return 1
    elif len(pelaaja1_alueet) < len(pelaaja2_alueet):
        return 2
    else:
        return 0

if __name__ == "__main__":
    # Testaus:
    pelilauta1 = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [0, 2, 2, 0],
        [2, 0, 0, 0]
    ]

    pelilauta2 = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [2, 2, 0, 0],
        [2, 2, 0, 0]
    ]

    print(kumpi_voitti(pelilauta1))  # Palauttaa 1, pelaaja 1 voitti
    print(kumpi_voitti(pelilauta2))  # Palauttaa 2, pelaaja 2 voitti
