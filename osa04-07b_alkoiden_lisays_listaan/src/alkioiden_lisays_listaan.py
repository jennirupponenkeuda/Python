# Kirjoita ratkaisu tähän
lukujen_maara = int(input("Kuinka monta lukua:"))
numerot = []

for i in range(lukujen_maara):
    luku = int(input(f"Anna luku {i + 1}: "))
    numerot.append(luku)

print(numerot)
