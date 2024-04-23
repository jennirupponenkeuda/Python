def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if 0 <= x <= 2 and 0 <= y <= 2 and lauta[y][x] == "":
        lauta[y][x] = nappula
        return True
    else:
        return False

if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)
