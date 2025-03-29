s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4, 5, 6}
s3 = {3, 5, 6, 7}
s4 = {6, 7, 8, 9}
s1.intersection(s2)   # czesc wspolna
s2.union(s1)   # suma obu
s3.difference(s2)  # roznica
s4.symmetric_difference(s1)  # suma obu z wykluczeniem czesci wspolnej
# _update zmieniaja set na nowy, bez tego zwracaja nowy
s1.issubset(s2)  # sprawdza czy jest podzbiorem
s1.issuperset(s2)  # sprawdza czy jest nadzbiorem
s1.isdisjoint(s2)  # sprawdza czy nie sa ze soba powiazane

# metody modyfikacji
s1.add(2)
s1.remove(1)
s1.discard(3)  # na cholere to nie zglasza bledu jak nie wystepuje
s1.pop()  # losowo ususwa element ze zbioru (pseudolosowo) -> element usuniety
s1.clear()  # usuwa wszystkie elementy
