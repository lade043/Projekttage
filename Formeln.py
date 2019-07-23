import Klassen as k

konstante_eins = k.Groesse(None, None, True, 1)

Formeln = [k.Formel('Kraftformel', i=k.Groesse('F', 'N', False), a=k.Groesse('m', 'kg', False),
                    b=k.Groesse('a', 'm/s²', False), z=k.Groesse(None, None, True, 1), y=k.Groesse(None, None, True, 1),
                    x=k.Groesse(None, None, True, 1)),
           k.Formel('Gleichm. beschl. Bew.', i=k.Groesse('s', 'm', False), a=k.Groesse(None, None, True, 0.5),
                    b=('a', 'm/s^2', False), c=k.Groesse('t', 's', False), z=konstante_eins, x=konstante_eins,
                    y=k.Groesse(None, None, True, 2)),
           k.Formel('Gewichtskraft', i=k.Groesse('Fg', 'N',False), a=k.Groesse(None,None,True,9.81),b=('h','m',False),
                    z=konstante_eins,y=konstante_eins,x=konstante_eins),
           k.Formel('Spannenergie', i=k.Groesse('Espann','J', False), a=k.Groesse(None, None, True, 0.5),
                    b=k.Groesse('D', '', False), c=k.Groesse('s', 'm', False), x=konstante_eins, y=konstante_eins,
                    z=k.Groesse(None, None, True, 2)),
           k.Formel("Potentielle Energie" , i=k.Groesse("Epot","J",False),b=k.Groesse("m","kg", False),
                    c=k.Groesse("Höhe","m",False), z=konstante_eins,y=konstante_eins,x=konstante_eins),
           k.Formel('Kinetische Energie',i=k.Groesse('Ekin','J', False), a=k.Groesse(None, None, True, 0.5),
                    b=('m', 'kg', False), c=('v', 'm/s', False), z=konstante_eins, x=konstante_eins,
                    y=k.Groesse(None, None, True, 2)),
           k.Formel('Elektrische Leistung', i=k.Groesse('P', 'W', False), a=k.Groesse('U', 'V', False),
                    b=k.Groesse('I','A', False), c=konstante_eins, z=konstante_eins, x=konstante_eins, y=konstante_eins)
           ]