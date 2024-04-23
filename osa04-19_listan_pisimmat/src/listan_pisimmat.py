# tee ratkaisu tänne
def pisimmat(lista):
    pisimmat_merkkijonot = []
    pituus = 0

    for merkkijono in lista:
        if len(merkkijono) > pituus:
            pisimmat_merkkijonot = [merkkijono]
            pituus = len(merkkijono)
        elif len(merkkijono) == pituus:
            pisimmat_merkkijonot.append(merkkijono)

    return pisimmat_merkkijonot

