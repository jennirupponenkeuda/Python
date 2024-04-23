# Kirjoita ratkaisu tähän
while True:    
    editori = input("Editori:").lower()
    if editori == "visual studio code":
        print("loistava valinta!")
        break
    elif editori == "word" or editori == "notepad":
        print("surkea")
    else:
        print("ei ole hyvä")
