n = int(input("A szám: "))

for i in range(1, n + 1):
    if n%i == 0:
        print(i)