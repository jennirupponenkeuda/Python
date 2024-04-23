# Kirjoita ratkaisu tähän
syonnit = int(input("Montako kertaa viikossa syöt Unicafessa?"))
hinta = float(input("Unicafe-lounaan hinta?"))
ruokaostokset = float(input("Paljonko käytät viikossa ruokaostoksiin?"))
paiva = (syonnit * hinta + ruokaostokset)/7
viikko = syonnit * hinta + ruokaostokset

print(f"Kustannukset keskimäärin:\nPäivässä {paiva} euroa\nViikossa {viikko} euroa")