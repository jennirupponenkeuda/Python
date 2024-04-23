# tee ratkaisu tänne
def vaihteluvali(lista):
    if not lista:
        return None  

    pienin = min(lista)
    suurin = max(lista)
    vali = suurin - pienin
    return vali


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [3, 6, -4] 
    tulos = vaihteluvali(lista) 
    print(tulos)