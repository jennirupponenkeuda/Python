# tee ratkaisu tänne
def uusi_henkilo(nimi: str, ika: int):
   
    if not nimi:
        raise ValueError("Nimi ei voi olla tyhjä merkkijono.")
    
    nimen_osat = nimi.split()
    if len(nimen_osat) < 2:
        raise ValueError("Nimen tulee koostua vähintään kahdesta sanasta.")
    
    if len(nimi) > 40:
        raise ValueError("Nimen pituus ei saa olla yli 40 merkkiä.")
    
   
    if ika < 0 or ika > 150:
        raise ValueError("Ikä tulee olla ei-negatiivinen luku ja enintään 150.")
    
    # Palauta henkilö-tuple
    return (nimi, ika)

