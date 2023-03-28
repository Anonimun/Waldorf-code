lista = ["alma", "kék", "én", "Zsák", "almafa","a"]
print(sorted(lista))
print(sorted(lista,key=len))
def aszam(szo):
    return szo.count("a")
print(sorted(lista,key=aszam, reverse=True))
print(sorted(lista,key=len))
