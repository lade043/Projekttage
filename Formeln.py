import Klassen as k

konstante_eins = k.Groesse(None, None, True, 1)

Formeln = [k.Formel('Kraftformel', "F=m*a", i=k.Groesse('F', 'N', False), a=k.Groesse('m', 'kg', False),
                    b=k.Groesse('a', 'm/s', False), c=konstante_eins, z=konstante_eins,
                    y=konstante_eins, x=konstante_eins),
           k.Formel('Gleichm. beschl. Bew.',"s=0.5*a*t^2", i=k.Groesse('s', 'm', False), a=k.Groesse(None, None, True, 0.5),
                    b=k.Groesse('a', 'm/s^2', False), c=k.Groesse('t', 's', False), z=konstante_eins, x=konstante_eins,
                    y=k.Groesse(None, None, True, 2)),
           k.Formel('Gewichtskraft',"Fg=9,81*h", i=k.Groesse('Fg', 'N',False), a=k.Groesse(None,None,True,9.81),b=k.Groesse('h','m',False),
                    c=konstante_eins, z=konstante_eins,y=konstante_eins,x=konstante_eins),
           k.Formel('Spannenergie',"Espann=0,5*D*s^2", i=k.Groesse('Espann','J', False), a=k.Groesse(None, None, True, 0.5),
                    b=k.Groesse('D', 'N/m', False), c=k.Groesse('s', 'm', False), x=konstante_eins, y=konstante_eins,
                    z=k.Groesse(None, None, True, 2)),
           k.Formel('Potentielle Energie',"Epot=m*9.81*h", i=k.Groesse('Epot','J',False),a=k.Groesse('m','kg', False),
                    b=k.Groesse(None, None, True, 9.81), c=k.Groesse('h','m',False), z=konstante_eins,
                    y=konstante_eins,x=konstante_eins),
           k.Formel('Kinetische Energie',"Ekin=0,5*m*v^2",i=k.Groesse('Ekin','J', False), a=k.Groesse(None, None, True, 0.5),
                    b=k.Groesse('m', 'kg', False), c=k.Groesse('v', 'm/s', False), z=konstante_eins, x=konstante_eins,
                    y=k.Groesse(None, None, True, 2)),
           k.Formel('Elektrische Leistung',"P=U*I", i=k.Groesse('P', 'W', False), a=k.Groesse('U', 'V', False),
                    b=k.Groesse('I','A', False), c=konstante_eins, z=konstante_eins, x=konstante_eins, y=konstante_eins),
           k.Formel("Geschwindigkeit",'v=s/t', i=k.Groesse ('v', 'm/s',False), a=k.Groesse('s', 'm', False),
                    b=k.Groesse ('t','s', False), z= konstante_eins, y= konstante_eins, x=k.Groesse(None,None,True,-1)),

           k.Formel('Wiederstand',"R=U/I", i=k.Groesse('R', 'Ohm', False), a=k.Groesse('U', 'V', False),
                    b=k.Groesse('I', 'A', False), c=konstante_eins, z=konstante_eins, y=k.Groesse(None, None, True, -1),
                    x=konstante_eins),
           k.Formel('Impuls',"p=m*v", i=k.Groesse('p', 'N*s', False), a=k.Groesse('m', 'kg', False),
                    b=k.Groesse('v', 'm/s', False), c=konstante_eins, z=konstante_eins, y=konstante_eins,
                    x=konstante_eins)
           ]


def looper(geg, ges):
    for formel in Formeln:
        temp_is_solvable = formel.is_solvable(geg, ges)
        if temp_is_solvable[0]:
            return formel.solve(temp_is_solvable[1], [geg, ges])
