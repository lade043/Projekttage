import Formeln
def user_Input():
    geg = {}
    ges = {}
    geginput = None
    gesinput = None

    while True:
        geginput = input("Welche Formelzeichen sind gegeben? Geben Sie immer nur EINS ein! \n Bestätigen sie Ihre Eingaben mit 'Fertig'\n")
        if geginput == "Fertig":
            for symbol in geg:
                geg[symbol] = float(input("Geben Sie den Wert zu " + symbol + " ein.\n"))
            break
        else:
            geg[geginput] = None

    gesinput = input("Welches Formelzeichen sind gesucht?\n")
    ges[gesinput] = None
    return [geg, ges]


def user_Output(liste):
    geg = liste[1][0]
    ges = liste[1][1]
    formel_str = liste[1][2].string
    formel_name = liste[1][2].name
    #einsetzen von ergebnis in ges
    ges[list(ges.keys())[0]] = liste[0]
    print("\n\n\n100% \nDas Programm hat fertig gerechnet!")
    print("Dies war gegeben: ")
    for wert in geg:
        print(wert + " = " + str(geg[wert]))
    print("\nDas was gesucht: ")
    for wert1 in ges:
        print(wert1 + " = " + str(ges[wert1]))
    print("\nDiese Formel habn wir genutzt: " + formel_name)
    print("So sieht die Formel aus: " + str(formel_str))
