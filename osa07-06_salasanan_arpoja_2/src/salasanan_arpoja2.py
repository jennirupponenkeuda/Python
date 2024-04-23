# tee ratkaisu tänne
import random
import string

def luo_hyva_salasana(pituus: int, numerot: bool, erikoismerkit: bool):
    kirjaimet = string.ascii_lowercase
    numerot_joukko = string.digits if numerot else ''
    erikoismerkit_joukko = '!?=+-()#' if erikoismerkit else ''
    
   
    kirjain = random.choice(kirjaimet)
    
    numero = random.choice(numerot_joukko) if numerot else ''
    
    
    erikoismerkki = random.choice(erikoismerkit_joukko) if erikoismerkit else ''
    
   
    loput = random.choices(kirjaimet + numerot_joukko + erikoismerkit_joukko, k=pituus - len(kirjain + numero + erikoismerkki))
    
   
    salasana = ''.join([kirjain, numero, erikoismerkki] + loput)
    salasana = ''.join(random.sample(salasana, len(salasana)))  # sekoita salasana
    
    return salasana


