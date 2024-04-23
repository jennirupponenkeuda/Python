# tee ratkaisu tänne

def kertomat(n: int):
    kertoma_dict = {}

    for i in range(1, n + 1):
        kertoma = 1
        for j in range(1, i + 1):
            kertoma *= j
        kertoma_dict[i] = kertoma    
    return kertoma_dict

def main():
    n = 2
    k = kertomat(n)

    for i in range(1, n + 1):
        print(f"{i}! = {k[i]}")
        
if __name__ == "__main__":
    main()