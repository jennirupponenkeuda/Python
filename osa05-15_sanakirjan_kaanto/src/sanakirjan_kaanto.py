# tee ratkaisu tänne
def kaanna(sanakirja: dict):
    kaannetty = {v: k for k, v in sanakirja.items()}
    sanakirja.clear()
    sanakirja.update(kaannetty)

if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)
