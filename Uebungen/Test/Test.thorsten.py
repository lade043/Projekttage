import random

geheimzahl = random.randrange(32)
ratezahl = 0

while ratezahl != geheimzahl:
    ratezahl = int(input("Raten Sie die geheime Zahl: "))

    if ratezahl > geheimzahl:
        print("Zu hoch")

    elif ratezahl < geheimzahl:
        print("Zu niedrig")

print("Herzlichen Glückwunsch! Die geheime Zahl war " + str(geheimzahl))
