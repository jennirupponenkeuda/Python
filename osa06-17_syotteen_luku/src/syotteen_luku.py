def lue(pyynto: str, ala: int, yla: int):
    while True:
        try:
            luku = int(input(pyynto))
            if ala <= luku <= yla:
                return luku
            elif luku < ala:
                print(f"Syötteen on oltava kokonaisluku väliltä {ala}...{yla}")
            elif luku > yla:
                print(f"Syötteen on oltava kokonaisluku väliltä {ala}...{yla}")
        except ValueError:
            print(f"Syötteen on oltava kokonaisluku väliltä {ala}...{yla}")

if __name__ == "__main__":
    luku = lue("syötä luku: ", 5, 10)
    print("syötit luvun:", luku)
