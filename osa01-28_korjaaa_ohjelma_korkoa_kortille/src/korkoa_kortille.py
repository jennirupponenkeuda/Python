# Korjaa ohjelma
pisteet = int(input("Kuinka paljon pisteitä? "))
if pisteet < 100:
    bonus = pisteet * 1.1
    print(f"Sait 10 % bonusta")
if pisteet >=100:
    bonus = pisteet * 1.15
    print(f"Sait 15 % bonusta")
print(f"Pisteitä on nyt {bonus}")
