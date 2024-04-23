def eniten_kirjainta(merkkijono):
    kirjaimet = {}
    
    for kirjain in merkkijono:
        if kirjain.isalpha():
            kirjain = kirjain.lower()
            if kirjain in kirjaimet:
                kirjaimet[kirjain] += 1
            else:
                kirjaimet[kirjain] = 1

    eniten_esiintynyt_kirjain = max(kirjaimet, key=lambda k: kirjaimet[k])
    return eniten_esiintynyt_kirjain

if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))

