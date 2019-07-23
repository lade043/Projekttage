import Klassen as k

konstante_eins = k.Groesse(None, None, True, 1)

Formeln = [k.Formel('Kraftformel', i=k.Groesse('F', 'N', False), a=k.Groesse('m', 'kg', False),
                    b=k.Groesse('a', 'm/s²', False), z=k.Groesse(None, None, True, 1), y=k.Groesse(None, None, True, 1),
                    x=k.Groesse(None, None, True, 1)),
           k.Formel('Gleichm. beschl. Bew.', i=k.Groesse('s', 'm', False), a=k.Groesse(None, None, True, 0.5),
                    b=('a', 'm/s^2', False), c=k.Groesse('t', 's', False), z=konstante_eins, x=konstante_eins,
                    y=k.Groesse(None, None, True, 2)),
            k.Formel('Kinetische Energie',i=k.Groesse('Ekin','J', False), a=k.Groesse(None, None, True, 0.5), b=('m', 'kg', False), c=('v', 'm/s', False), z=konstante_eins, x=konstante_eins, y=k.Groesse(None, None, True, 2))]
#Ekin=0,5*m*v^2
#f=m*a