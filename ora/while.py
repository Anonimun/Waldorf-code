ossz = 0
darab = -1
jegy = 5
while jegy != 0:
    jegy = int(input("hanyas? "))
    while jegy<0 or jegy>5:
        jegy= int(input("hibás kérem újra: "))
    ossz += jegy
    darab += 1
if darab>0:
    atlag = ossz/darab
    print("az átlagod: ", atlag)
else:
    print("nincs jegyed!")
