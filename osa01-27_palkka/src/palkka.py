# Kirjoita ratkaisu tähän
tuntipalkka = float(input("Tuntipalkka:"))
tyotunnit = float(input("Työtunnit:"))
viikonpaiva = str(input("Viikonpäivä:"))
if viikonpaiva == "sunnuntai":
    print(f"Palkka {tuntipalkka*2*tyotunnit} euroa")
if viikonpaiva != "sunnuntai":
    print(f"Palkka {tuntipalkka*tyotunnit} euroa")