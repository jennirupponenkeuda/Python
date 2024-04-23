# tee ratkaisu
from typing import List

def pisin(merkkijonot: List[str]) -> str:
    if not merkkijonot:
        return ""  

    pisin_merkkijono = merkkijonot[0] 

    for merkkijono in merkkijonot[1:]:
        if len(merkkijono) > len(pisin_merkkijono):
            pisin_merkkijono = merkkijono

    return pisin_merkkijono


