# tee ratkaisu tänne
def ika(syntymavuosi: int):
    nyt = 2023

    return nyt - syntymavuosi

def vanhin(henkilot: list):
    def syntymavuoden_laskeminen(henkilo):
        return ika(henkilo[1])
        
    vanhin_henkilo = max(henkilot, key=syntymavuoden_laskeminen)
    return vanhin_henkilo[0]


if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))