"""
t = (*"abcaba",)
print(t.count('a')) #->3
print(t.index("b")) #->1
print(t.index("a",2))

lis = [*"abcdefg"]
lis.append("h") #-> None
lis.insert(3,"!")#przed D wykrzyknik w index 3 przemieszcza reszte} Jeżeli index zbyt duży to doda na koniec
lis.insert(-3,"?")#przed element o indexie                               }
lis.extend("hij")#rozpakuje string na 3 znaki nie mozna podac 1 elementu musi byc kontener (moze byc 1 znakowy) Zwaraca None
#lis = lis + "zxc" - nie zadziala
#lis += "zxc" - zadziala (? += to operator extenda a nie to co wyzej)

lista = [1,2,3,4,"qwe"]
lista.remove("qwer") #usuwa po wartosci -->None
lista.pop()#usuwa po indexie --> zwraca co usunieto
lista.clear()
"""


# zadanie
# napiszcie program, ktory pobera dowolna ilosc liczb i zapsiuje do listy
lis = []
while True:
    x = input('Podaj liczbę:')
    if x == '':
        break
    lis.append(int(x))

print(lis)
