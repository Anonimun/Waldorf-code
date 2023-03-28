#tölzsd ki véletlen számokkal egylistát, és írd ki hogy páros, vagy páratlan, prím és rendezd az osztók száma szerint
import random
lista = []
def paritas(szam):
    if szam%2 == 0:
        return "páros"
    else:
        return "páratlan"
def osztoszam(szam):
    db=0
    for i in range(1,szam+1):
        if szam%i ==0:
            db+=1
    return db
def prim(szam):
    if osztoszam(szam)==2:
        return "prím"
    else:
        return "nem prím"
for i in range(100):
    lista.append(random.randint(0,100))
for szam in sorted(lista,key=osztoszam):
    print(szam,paritas(szam),prim(szam))
