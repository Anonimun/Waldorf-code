def prim(n):
    db = 0
    for i in range(1, n+1):
        if n%i == 0:
            db += 1
    if db == 2:
        return "prím"
    else:
        return "nem prím"

for i in range(1, 101):
    print(i, prim(i))