import random

geheimzahl = random.randrange(32)
zahl = 0



while zahl != geheimzahl:
    zahl = int(input("Geheimzahl ?"))


    if zahl > geheimzahl:
      print("Zahl zu groß")

    elif zahl < geheimzahl:
        print("Zahl zu klein")

print ("Du hast die Geheimzahl eraten, Die Geheimzahl war : "+ str (geheimzahl) )



