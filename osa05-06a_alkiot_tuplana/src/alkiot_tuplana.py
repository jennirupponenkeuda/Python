# tee ratkaisu tänne

def tuplaa_alkiot(luvut:list) -> list:
    tuplaluvut = []
    

    for alkio in luvut:
        tuplaluvut.append(alkio * 2)

    return tuplaluvut


if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)