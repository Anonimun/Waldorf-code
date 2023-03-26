szam1 = int(input("első szám: "))
szam2 = int(input("második szám: "))

for i in range(szam1*szam2, szam1-1, -1):
    if i%szam1==0 and i%szam2==0:
        lkkt = i

print("a legkissebb közös többszörös ", lkkt)