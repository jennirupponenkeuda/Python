# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
def palindromi(sana):
    sana = sana.lower().replace(" ", "")  # Muunnetaan kaikki kirjaimet pieniksi ja poistetaan välilyönnit
    return sana == sana[::-1]

if __name__ == "__main__":
    while True:
        kayttajan_syote = input("Anna palindromi: ")
        if palindromi(kayttajan_syote):
            print(f"{kayttajan_syote} on palindromi!")
            break
        else:
            print("ei ollut palindromi")

