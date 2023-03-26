import random
for i in range(1, 101):
    szam = random.randint(0,100)
    print(szam, end=" ")
    if i%10 == 0:
        print()