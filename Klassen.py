from copy import deepcopy
import math


class Groesse:
    def __init__(self, formelsymbol, einheit, konst, wert=None):
        self.formelsymbol = formelsymbol
        self.einheit = einheit
        self.wert = wert
        self.konst = konst
        self.equals_var = None

    def set(self, wert):
        self.wert = wert

    def set_equals_var(self, var):
        self.equals_var = var


class Formel:
    class Solver:
        def __init__(self, formel):
            self.formel = formel

        def _solve_to_i(self):
            return (self.formel.a**self.formel.z) * (self.formel.b**self.formel.y) * (self.formel.c**self.formel.x) + self.formel.d * self.formel.e * self.formel.f + self.formel.g

        def _solve_to_a(self):
            return ((self.formel.b**self.formel.y) * (self.formel.c**self.formel.x) + self.formel.d * self.formel.e *self.formel.f + self.formel.g * self.formel.i)**1/self.formel.z

        def _solve_to_b(self):
            return ((self.formel.a**self.formel.z) * (self.formel.c**self.formel.x) +self.formel.d *self.formel.e *self.formel.f + self.formel.g)**1/self.formel.y

        def _solve_to_c(self):
            return ((self.formel.a**self.formel.z) * (self.formel.b**self.formel.y) + self.formel.d *self.formel.e *self.formel.f +self.formel.g * self.formel.i)**1/self.formel.x

        def _solve_to_d(self):
            return self.formel.i - self.formel.g - (self.formel.a**self.formel.z) * (self.formel.b**self.formel.y)* (self.formel.c**self.formel.x) / self.formel.e * self.formel.f

        def _solve_to_e(self):
            return self.formel.i - self.formel.g - (self.formel.a**2) * (self.formel.b**self.formel.y) * (self.formel.c**self.formel.x) / self.formel.d * self.formel.f

        def _solve_to_f(self):
            return (self.formel.i-self.formel.g-(self.formel.a**self.formel.z)*(self.formel.b**self.formel.y)*(self.formel.c**self.formel.x)) / (self.formel.d * self.formel.e)

        def _solve_to_g(self):
            return - ((self.formel.a**self.formel.z) * (self.formel.b**self.formel.y) * (self.formel.c**self.formel.x) + self.formel.d * self.formel.e * self.formel.f - self.formel.i)

        def _solve_to_z(self):
            return math.log((self.formel.i-self.formel.d*self.formel.e*self.formel.f-self.formel.g) / ((self.formel.b**self.formel.y) * (self.formel.c**self.formel.x)), self.formel.a)

        def _solve_to_y(self):
            return math.log((self.formel.i-self.formel.d*self.formel.e*self.formel.f-self.g)/((self.formel.a**self.formel.z) * (self.formel.c**self.formel.x)), self.formel.b)

        def _solve_to_x(self):
            return math.log(self.formel.i-self.formel.d*self.formel.e*self.formel.f-self.formel.g)/(self.formel.a**self.formel.z)*(self.formel.b**self.formel.y, self.formel.c)

    def __init__(self, name, i, a=Groesse(None, None, True, 0), b=Groesse(None, None, True, 0),
                 c=Groesse(None, None, True, 0), d=Groesse(None, None, True, 0), e=Groesse(None, None, True, 0),
                 f=Groesse(None, None, True, 0), g=Groesse(None, None, True, 0), z=Groesse(None, None, True, 0),
                 y=Groesse(None, None, True, 0), x=Groesse(None, None, True, 0)):
        self.a = a
        self.a.set_equals_var('a')
        self.b = b
        self.b.set_equals_var('b')
        self.c = c
        self.c.set_equals_var('c')
        self.d = d
        self.d.set_equals_var('d')
        self.e = e
        self.e.set_equals_var('e')
        self.f = f
        self.f.set_equals_var('f')
        self.g = g
        self.g.set_equals_var('g')
        self.z = z
        self.z.set_equals_var('z')
        self.y = y
        self.y.set_equals_var('y')
        self.x = x
        self.x.set_equals_var('x')
        self.name = name
        self.i = i
        self.i.set_equals_var('i')
        self.liste = []
        self.solver = self.Solver(self)
        for var in [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.z, self.y, self.x, self.i]:
            if var.konst is False:
                self.liste.append(var)

    def is_solvable(self, geg, ges):
        temp_liste = deepcopy(self.liste)
        for geg_element in geg:
            for liste_element in temp_liste:
                # serach for element with fitting formelsymbol and then del it
                pass
        if len(temp_liste) == 1 and ges[0] == temp_liste[0]: # has to be changed accordingly
            return [True, temp_liste[0]]
        return [False, None]

    def solve(self, ges):
        if 'i' == ges.equals_var:
            self.solver._solve_to_i()
        elif 'e' == ges.equals_var:
            self.solver._solve_to_e()
        elif 'c' == ges.equals_var:
            self.solver._solve_to_c()
        elif 'b' == ges.equals_var:
            self.solver._solve_to_b()
        elif 'a' == ges.equals_var:
            self.solver._solve_to_a()
        elif 'x' == ges.equals_var:
            self.solver._solve_to_x()
        elif 'd' == ges.equals_var:
            self.solver. solve_to_d()


    def _solve_to_i(self):
        pass





math.sqrt()
