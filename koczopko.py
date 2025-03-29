# funkcja przyjmie liste i wyswietli kwadraty elementow
def kwadraty(l):
    for i in l:
        print(i * i)


# funkcja, która sprawdzi wszystkie elementy listy czy sa parzyste jak nie to false
def parzyste(l):
    for i in l:
        if i % 2 == 1:
            return False
    return True


lista = [2, 4]
lista2 = [1, 2, 3, 4]
# kwadraty(lista)
print(parzyste(lista))
print(parzyste(lista2))
