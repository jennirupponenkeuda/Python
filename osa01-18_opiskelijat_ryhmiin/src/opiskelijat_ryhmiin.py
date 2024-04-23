# Kirjoita ratkaisu tähän
opiskelijoiden_maara = int(input("Montako opiskelijaa?"))

ryhman_koko = int(input("Mikä on ryhmän koko?"))

ryhmien_maara = opiskelijoiden_maara // ryhman_koko

ylimaarainen = opiskelijoiden_maara % ryhman_koko

if ylimaarainen == 0:
    print(f"Ryhmien määrä: {ryhmien_maara}")

else:
    print(f"Ryhmien määrä: {ryhmien_maara + 1}")