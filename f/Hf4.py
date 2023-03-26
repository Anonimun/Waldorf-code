n = int(input("A szám: "))
oszto = []

for i in range(1, n + 1):
    if n % i == 0:
        oszto.append(i)

oszto_n = len(oszto)
print("a szám osztóinak a száma: ", oszto_n)
