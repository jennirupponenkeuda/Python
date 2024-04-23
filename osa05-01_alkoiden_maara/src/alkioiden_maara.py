# tee ratkaisu tänne
def laske_alkiot(matriisi: list, alkiot: int):
    maara = 0
    for rivi in matriisi:
        for arvo in rivi:
            if arvo == alkiot:
                maara += 1
    return maara

if __name__ == "__main__":
    matriisi = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    vastaus = laske_alkiot(matriisi, 1)
    print(vastaus)