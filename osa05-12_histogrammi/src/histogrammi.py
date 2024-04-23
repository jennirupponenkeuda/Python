# tee ratkaisu tänne
def histogrammi (merkkijono):
    laskuri = {}

    for kirjain in merkkijono:
        laskuri[kirjain] = laskuri.get(kirjain, 0) + 1
    for kirjain, maara in laskuri.items():
        print(f"{kirjain} {'*' * maara}")