def muotoile(lista):
    muotoillut_luvut = [f'{luku:.2f}' for luku in lista]
    return muotoillut_luvut

if __name__ == "__main__":
    alkuperainen_lista = [0.123, 1.23, 0.0234]
    muotoiltu_lista = muotoile(alkuperainen_lista)

    for luku in muotoiltu_lista:
        print(luku)
