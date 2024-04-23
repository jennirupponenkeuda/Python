# tee ratkaisu tänne
def lyhin(lista):
    if not lista:
        return 0
    lyhin_sana = min(lista, key=len)

    return lyhin_sana