dic = {1: 2, 3: 3, 4: 6}
print(dic)
dic.pop(3)
dic.popitem()  # usuwa ostatnie elementy ze slownika
print(dic)
dic.setdefault('t', 'l')  # mozna nadpisac klucz
print(dic)
dic.update({3: 'b', 'e': 'ł☻'})  # nie mozna nadpisac wartosci klucza
print(dic)
dic['B'] = 'G'
print(dic)
print(dic.keys(), dic.values(), dic.items())  # klucze  # wartosci  # krotki
print(
    dic.get('H', 0)
)  # wyciaga wartosc po kluczu, kiedy nie ma wartosci zwraca 0
print(dic['t'])  # zwraca blad jak nie znajdzie klucza
