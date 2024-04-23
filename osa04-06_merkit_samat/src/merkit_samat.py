# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def samat(merkkijono, indeksi1, indeksi2):
    if 0 <= indeksi1 < len(merkkijono) and 0 <= indeksi2 < len(merkkijono):
        return merkkijono[indeksi1] == merkkijono[indeksi2]
    
    else:
        return False

if __name__ == "__main__":
    print(samat("koodari", 1, 2))