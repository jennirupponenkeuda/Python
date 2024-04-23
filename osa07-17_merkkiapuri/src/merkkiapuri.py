# tee ratkaisu tänne
# merkkiapuri.py

def vaihda_koko(merkkijono: str) -> str:
    """Vaihtaa merkkijonon isot kirjaimet pieniksi ja päinvastoin."""
    return merkkijono.swapcase()

def puolita(merkkijono: str):
    pituus = len(merkkijono)
    puolikas = pituus // 2
    ensimmainen_osuus = merkkijono[:puolikas]
    toinen_osuus = merkkijono[puolikas:]

    return ensimmainen_osuus, toinen_osuus

def poista_erikoismerkit(merkkijono: str) -> str:
    """Poistaa merkkijonosta kaikki erikoismerkit paitsi aakkoset, numerot ja välilyönnit."""
    puhdistettu = ''.join(char for char in merkkijono if char.isalnum() or char.isspace())
    return puhdistettu

# Testaus
if __name__ == "__main__":
    mjono = "Moi kaikki!"
    
    
    muutettu_mjono = vaihda_koko(mjono)
    print(muutettu_mjono)

 
    p1, p2 = puolita(mjono)
    print(p1)
    print(p2)

    
    puhdistettu_mjono = poista_erikoismerkit("Tämä on testi, katsotaan miten käy!!!11!")
    print(puhdistettu_mjono)
