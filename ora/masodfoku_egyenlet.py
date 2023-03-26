
import math

print("A program csakis a hagyományos(axˇ2+bx+cx) alakot fogadja el, és csak egyenlettel megoldható alakot írjon!")
print("Ha nem egész számokat ad meg a vessző helyett pontot írjon. ")
a = float(input("kérem az A számot"))
b = float(input("kérem az B számot"))
c = float(input("kérem az C számot"))
D = (b**2)-(4*a*c)
if D >= 0:
    x1 = (-b) + (math.sqrt(b ** 2 - (4 * a * b))) / (a * 2)
    x2 = (-b) - (math.sqrt(b ** 2 - (4 * a * b))) / (a * 2)
    print("x1 = ", x1)
    print("x2 = ", x2)
else:
    print('A diszkrimináns negatív. Nincs megoldás')
