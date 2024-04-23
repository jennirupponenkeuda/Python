sanat = []

while True:
    sana = input("sana: ")

    if sana in sanat:
        print(f"Annoit {len(sanat)} eri sanaa")
        break

    sanat.append(sana)
