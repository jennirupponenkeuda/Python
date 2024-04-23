def suodata_laskut():
    with open("laskut.csv") as tiedosto:
        oikeat_rivit = []
        vaarat_rivit = []

        for rivi in tiedosto:
            nimi, lasku, tulos = rivi.strip().split(";")
            operandit = lasku.split("+") if "+" in lasku else lasku.split("-")
            operandit = [int(operand) for operand in operandit]

            if eval(f"{operandit[0]}{'' if '+' in lasku else '-'}{operandit[1]}") == int(tulos):
                oikeat_rivit.append(rivi.strip())
            else:
                vaarat_rivit.append(rivi.strip())

    with open("oikeat.csv", "w") as oikeat_tiedosto:
        oikeat_tiedosto.write("\n".join(oikeat_rivit))

    with open("vaarat.csv", "w") as vaarat_tiedosto:
        vaarat_tiedosto.write("\n".join(vaarat_rivit))

# Test the function
suodata_laskut()
