lista1 = [1,2,5,6,10,0,-1,1,2,5,1,2,9]
lista2 = list()
lista1.append(100)
print(lista1)
print("egyesek száma: ", lista1.count(1))
print("második eleme: ",lista1[1])
print("utolsó eleme: ", lista1[-1])
print("hanyadik eleme a 10-es: ", lista1.index(10))
if 9 in lista1:
    print("ha 9 eleme, hanyadik eleme a 9-es: ", lista1.index(9))
else:
    print("nincs benne 9-es! ")
for szam in lista1:
    print(szam)
#ugyanaz a lista marad csak 2 néven
#lista2 = lista1
#mindig másolni kell, ha új listát akarunk
lista2 = lista1.copy()
lista1.append(99)
print(lista2)
#végleges rendezés
lista1.sort()
print(lista1)
lista1.sort(reverse=True)
print(lista1)
#rendezve írom ki
for szam in sorted(lista2,reverse=True):
    print(szam)
print(lista2)
print(max(lista2))

