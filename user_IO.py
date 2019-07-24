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


