import Formeln
import user_IO
import Klassen
while True:
    dicts = user_IO.user_input()
    ret = Formeln.looper(dicts[0], dicts[1])
    user_IO.user_output(ret)
