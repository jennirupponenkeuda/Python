# tee ratkaisu tänne
from fractions import Fraction

def jaa_palasiksi(maara: int):
    if maara <= 0:
        raise ValueError("Palasten määrän tulee olla positiivinen luku")

    # Käytetään fractions.Fraction jakamaan 1 yhtä suuriin osiin
    osa = Fraction(1, maara)
    
    # Palautetaan lista murtolukuja
    return [osa for _ in range(maara)]

if __name__ == "__main__":
    for p in jaa_palasiksi(3):
        print(p)

