class Depozyt:
    def __init__(self, zloto, srebro):
        self.srebro = srebro
        self.zloto = zloto

    def polacz(self, dep1):
        self.srebro = self.srebro + dep1.srebro
        self.zloto = self.zloto + dep1.zloto
        dep1.zloto = 0
        dep1.srebro = 0


d1 = Depozyt(1, 3)
d2 = Depozyt(0.5, 3)
d1.polacz(d2)

print(d1.zloto, d1.srebro, d2.zloto, d2.srebro)
