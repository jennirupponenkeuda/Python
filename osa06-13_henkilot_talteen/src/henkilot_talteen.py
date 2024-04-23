# tee ratkaisu tänne
def tallenna_henkilo(henkilo: tuple):
    nimi, ika, pituus = henkilo

    with open("henkilot.csv", "a") as tiedosto:
        tiedosto.write(f"{nimi};{ika};{pituus}\n")

if __name__=="__main__":
    tallenna_henkilo("Kimmo Kimmonen", 37, 175.5)
