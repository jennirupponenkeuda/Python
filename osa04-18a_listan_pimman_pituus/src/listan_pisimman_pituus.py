# tee ratkaisu tänne
def pisimman_pituus(lista):
    if not lista:
        return 0
    pisin_sana = max(lista, key=len)

    return len(pisin_sana)