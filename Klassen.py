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
            self.dicts = []

        def set_geg(self):
            for element in self.dicts[0]:
                for element1 in self.formel.liste:
                    if element == element1.formelsymbol:
                        element1.set(self.dicts[0][element])

        def set_dicts(self, dicts):
            self.dicts = dicts

        def get_dicts(self):
            return self.dicts

        def solve_to_i(self):
            return [(self.formel.a.wert**self.formel.z.wert) * (self.formel.b.wert**self.formel.y.wert) * (self.formel.c.wert**self.formel.x.wert) + self.formel.d.wert * self.formel.e.wert * self.formel.f.wert + self.formel.g.wert, self.get_dicts()]

        def solve_to_a(self):
            return [((self.formel.b.wert**self.formel.y.wert) * (self.formel.c.wert**self.formel.x.wert) + self.formel.d.wert * self.formel.e.wert *self.formel.f.wert + self.formel.g.wert * self.formel.i.wert)**1/self.formel.z.wert, self.get_dicts()]

        def solve_to_b(self):
            return [((self.formel.i.wert - self.formel.d.wert * self.formel.e.wert * self.formel.f.wert - self.formel.g.wert)/((self.formel.a.wert ** self.formel.z.wert) * (self.formel.c.wert ** self.formel.x.wert)))**(1/self.formel.y.wert), self.get_dicts()]

        def solve_to_c(self):
            return [((self.formel.i.wert - self.formel.d.wert * self.formel.e.wert * self.formel.f.wert - self.formel.g.wert) / ((self.formel.a.wert ** self.formel.z.wert) * (self.formel.b.wert ** self.formel.y.wert))) ** (1 / self.formel.y.wert), self.get_dicts()]

        def solve_to_d(self):
            return [self.formel.i.wert - self.formel.g.wert - (self.formel.a**self.formel.z.wert) * (self.formel.b**self.formel.y.wert)* (self.formel.c.wert**self.formel.x.wert) / self.formel.e.wert * self.formel.f.wert, self.get_dicts()]

        def solve_to_e(self):
            return [self.formel.i.wert - self.formel.g.wert - (self.formel.a.wert**2) * (self.formel.b.wert**self.formel.y.wert) * (self.formel.c.wert**self.formel.x.wert) / self.formel.d.wert * self.formel.f.wert, self.get_dicts()]

        def solve_to_f(self):
            return [(self.formel.i.wert-self.formel.g.wert-(self.formel.a.wert**self.formel.z.wert)*(self.formel.b.wert**self.formel.y.wert)*(self.formel.c.wert**self.formel.x.wert)) / (self.formel.d.wert * self.formel.e.wert), self.get_dicts()]

        def solve_to_g(self):
            return [- ((self.formel.a.wert**self.formel.z.wert) * (self.formel.b.wert**self.formel.y.wert) * (self.formel.c.wert**self.formel.x.wert) + self.formel.d.wert * self.formel.e.wert * self.formel.f.wert - self.formel.i.wert), self.get_dicts()]

        def solve_to_z(self):
            return [math.log((self.formel.i.wert-self.formel.d.wert*self.formel.e.wert*self.formel.f.wert-self.formel.g.wert) / ((self.formel.b.wert**self.formel.y.wert) * (self.formel.c.wert**self.formel.x.wert)), self.formel.a.wert), self.get_dicts()]

        def solve_to_y(self):
            return [math.log((self.formel.i.wert-self.formel.d.wert*self.formel.e.wert*self.formel.f.wert-self.formel.g.wert)/((self.formel.a.wert**self.formel.z.wert) * (self.formel.c.wert**self.formel.x.wert)), self.formel.b.wert), self.get_dicts()]

        def solve_to_x(self):
            return [math.log(self.formel.i.wert-self.formel.d.wert*self.formel.e.wert*self.formel.f.wert-self.formel.g.wert)/(self.formel.a.wert**self.formel.z.wert)*(self.formel.b.wert**self.formel.y.wert, self.formel.c.wert), self.get_dicts()]

    def __init__(self, name, grundform, i, a=Groesse(None, None, True, 0), b=Groesse(None, None, True, 0),
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
        self.string = grundform
        self.solver = self.Solver(self)
        for var in [self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.z, self.y, self.x, self.i]:
            if var.konst is False:
                self.liste.append(var)

    def is_solvable(self, geg, ges):
        temp_liste = deepcopy(self.liste)
        for geg_element in geg:
            for i, liste_element in enumerate(temp_liste):
                if geg_element == liste_element.formelsymbol:
                    temp_liste.pop(i)
        if len(temp_liste) == 1 and list(ges.keys())[0] == temp_liste[0].formelsymbol:
            return [True, temp_liste[0]]
        return [False, None]

    def solve(self, ges, dicts):
        temp_dicts = dicts
        temp_dicts.append(self)
        ret = None
        self.solver.set_dicts(temp_dicts)
        self.solver.set_geg()
        if 'i' == ges.equals_var:
            ret = self.solver.solve_to_i()
        elif 'e' == ges.equals_var:
            ret = self.solver.solve_to_e()
        elif 'c' == ges.equals_var:
            ret = self.solver.solve_to_c()
        elif 'b' == ges.equals_var:
            ret = self.solver.solve_to_b()
        elif 'a' == ges.equals_var:
            ret = self.solver.solve_to_a()
        elif 'x' == ges.equals_var:
            ret = self.solver.solve_to_x()
        elif 'd' == ges.equals_var:
            ret = self.solver. solve_to_d()
        elif 'e' == ges.equals_var:
            ret = self.solver. solve_to_e()
        elif 'f' == ges.equals_var:
            ret = self.solver. solve_to_f()
        elif 'g' == ges.equals_var:
            ret = self.solver. solve_to_g()
        elif 'y' == ges.equals_var:
            ret = self.solver. solve_to_y()
        elif 'z' == ges.equals_var:
            ret = self.solver. solve_to_z()

        return ret


