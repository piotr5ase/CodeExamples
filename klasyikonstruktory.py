"""
class  tworzy nowa klase
class Dog: z wielkiej litery
    age=8 atrybuty - zmienne w klasie
    race="beagle" atrybuty

fifi = Dog()
print(fifi.age)

type
"""


class Dog:
    glos = ''

    # metody wewnatrz obiektu funkcja, init uruchamia sie przy utworzeniu moga byc argsy quarksy i inne metody zawsze powinien byc
    def __init__(self, glos):
        self.glos = glos

    def daj_glos(self):
        print(self.glos)


class Candidate:
    glosy = 0

    def oddaj_glos(self):
        self.glosy = self.glosy + 1


IllegalAlien = Candidate()
CatLady = Candidate()
SleepyJoe = Candidate()

IllegalAlien.oddaj_glos()
IllegalAlien.oddaj_glos()
CatLady.oddaj_glos()

print(IllegalAlien.glosy, CatLady.glosy, SleepyJoe.glosy)

# Pies = Dog("woof")
# Pies.daj_glos()

# fifi = Dog("hał hał")
# fifi.daj_glos()
