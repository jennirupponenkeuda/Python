# Kirjoita ratkaisu tähän
while True:
    print(f"Lista on nyt {lista}")

    valinta = input("(l)isää, (p)oista vai e(x)it: ")
    print(f"Valittu toiminto: {valinta}")

    if valinta == "l":
        lisattava = 1 if not lista else lista[-1] + 1
        lista.append(lisattava)
    elif valinta == "p":
        if lista:
            lista.pop()
    elif valinta == "x":
        print("Moi!")
        break
    else:
        print("Virheellinen valinta. Yritä uudelleen.")

