import random

ismetles = "y"
while ismetles == "y":
    maxrand = int(input("Válazd ki a maximum számot: "))
    szam = random.randint(0, maxrand)
    print("Találd ki a titkos számot!")
    kitalalva = 0
    while kitalalva == 0:
        sejtes = int(input("Mit sejtesz, mi a szám? "))
        if sejtes == szam:
            print("gratulálok! Kitaláltad a számot! ")
            kitalalva += 1
        elif sejtes < szam:
            print("A titkos szám NAGYOBB mint a sejtésed!")
        elif sejtes > szam:
            print("A titkos szám KISEBB mint a sejtésed!")
        else:
            print("Érvénytelen érték!")
    ismetles = input("Akarsz mégegyszer játszani? (y/n) ")
print("\n\nKöszönöm, hogy játszottál!\nKészítette: Márkus Dávid")
