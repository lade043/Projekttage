import Klassen as k

konstante_eins = k.Groesse(None, None, True, 1)

Formeln = [k.Formel('Kraftformel', "F=m*a", i=k.Groesse('F', 'N', False), a=k.Groesse('m', 'kg', False),
                    b=k.Groesse('a', 'm/s²', False), c=konstante_eins, z=konstante_eins,
                    y=konstante_eins, x=konstante_eins),
           k.Formel('Gleichm. beschl. Bew.', i=k.Groesse('s', 'm', False), a=k.Groesse(None, None, True, 0.5),
                    b=('a', 'm/s^2', False), c=k.Groesse('t', 's', False), z=konstante_eins, x=konstante_eins,
                    y=k.Groesse(None, None, True, 2)),
           k.Formel('Gewichtskraft', i=k.Groesse('Fg', 'N',False), a=k.Groesse(None,None,True,9.81),b=('h','m',False),
                    c=konstante_eins, z=konstante_eins,y=konstante_eins,x=konstante_eins),
           k.Formel('Spannenergie', i=k.Groesse('Espann','J', False), a=k.Groesse(None, None, True, 0.5),
                    b=k.Groesse('D', 'N/m', False), c=k.Groesse('s', 'm', False), x=konstante_eins, y=konstante_eins,
                    z=k.Groesse(None, None, True, 2)),
           k.Formel('Potentielle Energie',"Epot=m*g*h", i=k.Groesse('Epot','J',False),a=k.Groesse('m','kg', False),
                    b=k.Groesse(None, None, True, 9.81), c=k.Groesse('h','m',False), z=konstante_eins,
                    y=konstante_eins,x=konstante_eins),
           k.Formel('Kinetische Energie',i=k.Groesse('Ekin','J', False), a=k.Groesse(None, None, True, 0.5),
                    b=('m', 'kg', False), c=('v', 'm/s', False), z=konstante_eins, x=konstante_eins,
                    y=k.Groesse(None, None, True, 2)),
           k.Formel('Elektrische Leistung', i=k.Groesse('P', 'W', False), a=k.Groesse('U', 'V', False),
                    b=k.Groesse('I','A', False), c=konstante_eins, z=konstante_eins, x=konstante_eins, y=konstante_eins),
           k.Formel("Geschwindigkeit",'v=s/t', i=k.Groesse ('v', 'm/s',False), a=k.Groesse('s', 'm', False),
                    b=k.Groesse ('t','s', False), z= konstante_eins, y= konstante_eins, x=k.Groesse(None,None,True,-1)),

           k.Formel('Wiederstand', i=k.Groesse('R', 'Ohm', False), a=k.Groesse('U', 'V', False),
                    b=k.Groesse('I', 'A', False), c=konstante_eins, z=konstante_eins, y=k.Groesse(None, None, True, -1),
                    x=konstante_eins),
           k.Formel('Impuls', i=k.Groesse('p', 'N*s', False), a=k.Groesse('m', 'kg', False),
                    b=k.Groesse('v', 'm/s', False), c=konstante_eins, z=konstante_eins, y=konstante_eins,
                    x=konstante_eins)
           ]


def looper(geg, ges):
    for formel in Formeln:
        temp_is_solvable = formel.is_solvable(geg, ges)
        if temp_is_solvable[0]:
            formel.solve(temp_is_solvable[1], [geg, ges])