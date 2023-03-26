def pos(szoveg):
    n = int(input(szoveg))
    while n <= 0:
        n = int(input("hiba újra"))
    return n
#def-nek legyen return funkciója
def kiir(n):
    print("terület = ", n)

a = pos("A oldal")
b = pos("B oldal")

t = a*b
kiir(t)