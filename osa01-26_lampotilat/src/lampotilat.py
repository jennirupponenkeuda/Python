# Kirjoita ratkaisu tähän
fahrenheit =  float(input("Anna lämpötila (F):"))
# muunto-ohje  °C = (°F − 32) / 1,8.
celcius = (fahrenheit - 32) / 1.8
print(f"{fahrenheit} fahrenheit-astetta on {celcius} celsius-astetta")
if celcius < 0:
    print("Paleltaa!")
 