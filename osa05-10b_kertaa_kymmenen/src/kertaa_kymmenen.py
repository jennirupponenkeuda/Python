# tee ratkaisu tänne
def kertaa_kymmenen(alku: int, loppu: int):
    sanakirja = {}
    for avain in range(alku, loppu + 1):
        sanakirja[avain] = avain * 10
    return sanakirja

if __name__ == "__main__":
    d = kertaa_kymmenen(1, 2)
    print(d)
