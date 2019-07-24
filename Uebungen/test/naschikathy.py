import random
geheimzahl =random.randrange(40)
zahl = 0

while zahl != geheimzahl:
    zahl = int(input ('Errate die Zahl!!'))

    print ("Errate die Zahl!!")
    print (zahl)

    if zahl>geheimzahl:
        print ("zu groß")

    elif zahl<geheimzahl:
        print ("zu kleen")

    else:
        print ("JÖAR GANZ GENAU!!!")