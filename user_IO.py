def user_Input():
    geg = {}
    ges = {}
    geginput = None
    gesinput = None

    while True:
        geginput = input("Welche Formelzeichen sind gegeben? Geben Sie immer nur EINS ein! \n Bestätigen sie Ihre Eingaben mit 'Fertig'\n")
        if geginput == "Fertig":
            for symbol in geg:
                geg[symbol] = float(input("Geben Sie den Wert zu " + symbol + " ein."))
            break
        else:
            geg[geginput] = None

    gesinput = input("Welches Formelzeichen sind gesucht?")
    ges[gesinput] = None
    return [geg, ges]

def user_Output(geg, ges, formelname, formelaufbau):
    print("100% \nDas Programm hat fertig gerechnet!")
    print("Dies war gegeben: ")
    for wert in geg:
        print(wert + " = " + str(geg[wert]))
    print("\nDas was gesucht: ")
    for wert1 in ges:
        print(wert1 + " = " + ges[wert1])
    print("\nDiese Formel habn wir genutzt: " + formelname)
    print("So sieht die Formel aus: " + str(formelaufbau))
