import random
import string

def luo_salasana(pituus: int):
    kirjaimet = string.ascii_lowercase
    salasana = ''.join(random.choices(kirjaimet, k=pituus))
    return salasana

if __name__ == "__main__":
    
    for i in range(10):
        print(luo_salasana(8))
