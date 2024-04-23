# tee ratkaisu tänne
def tee_tuple(x: int, y: int, z: int):
    pienin = min(x,y,z)
    suurin = max(x,y,z)
    summa = x + y + z

    tuple = (pienin, suurin, summa)
    return tuple
if __name__ == "__main__":
    print(tee_tuple(5,3,-1))