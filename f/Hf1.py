n = int(input("A maximum szám: "))

if n >= 0:
    for i in range(1, n):
        print(i)
else:
    for i in range(1, n, -1):
        print(i)