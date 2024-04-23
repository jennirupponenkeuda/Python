# tee ratkaisu tänne
def kaikki_vaarinpain(lista):
    vaarinpain_lista = [sana[::-1] for sana in lista][::-1]
    return vaarinpain_lista


if __name__ == "__main__":
    alkuperainen_lista = ["Moi", "kaikki", "esimerkki", "vielÃ¤ yksi"]
    alkuperainen_lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    vaarinpain_lista = kaikki_vaarinpain(alkuperainen_lista)
    print(vaarinpain_lista)
