class Formel:
    def __init__(self, name, i, a=Groesse(None, None, True, 0), b=Groesse(None, None, True, 0),
                 c=Groesse(None, None, True, 0), d=Groesse(None, None, True, 0), e=Groesse(None, None, True, 0),
                 f=Groesse(None, None, True, 0), g=Groesse(None, None, True, 0), z=Groesse(None, None, True, 0),
                 y=Groesse(None, None, True, 0), x=Groesse(None, None, True, 0)):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.z = z
        self.y = y
        self.x = x
        self.name = name
        self.i = i
        self.liste = []
        for var in [self.a, self.b, self.c]:
            if var.konst is False:
                self.liste.append(var)


class Groesse:
    def __init__(self, formelsymbol, einheit, konst, wert=None):
        self.formelsymbol = formelsymbol
        self.einheit = einheit
        self.wert = wert
        self.konst = konst