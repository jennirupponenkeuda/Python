# tee ratkaisu tänne
def poista_pienin(luvut:list) -> None:
    if luvut:
        pienin_alkio = min(luvut)
        luvut.remove(pienin_alkio)





if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)