class Tegla:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def terulet(self):
        return self.a * self.b

    def kerulet(self):
        return 2 * (self.a + self.b)

    def __repr__(self):
        return f"A = {self.a}, B = {self.b}"


t1 = Tegla(2, 2)
print(t1)
