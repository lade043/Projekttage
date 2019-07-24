import random
geheimzahl=random.randrange(30)
Zahl=0

while Zahl != geheimzahl :
    Zahl = int(input ("Errate die Zahl"))
    if Zahl>geheimzahl:
        print("zu groß du Lappen")


    elif Zahl<geheimzahl:
        print("zu klein")
    else:
        print("du hast die Zahl erraten")