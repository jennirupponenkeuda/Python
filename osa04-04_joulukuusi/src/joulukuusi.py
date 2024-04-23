# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def joulukuusi(koko):
    print("joulukuusi!")
    for i in range(1, koko * 2, 2):
        tyhjat_valilyonnit = " " * ((koko * 2 - i) // 2)
        tahtia = "*" * i
        print(tyhjat_valilyonnit + tahtia)

    # Alimman "neulastason" tulostus
    print(" " * (koko - 1) + "*")





if __name__ == "__main__":
    joulukuusi(5)