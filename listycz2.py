lis = [1, 2, 3, 4, 56, 5.3, '3.1']
print(lis)
lis.reverse()
print(lis)
lis.sort(
    key=float
)  # a>b, oba skladniki musza pasowac do operatora wiec 2<a nie działa
# argumeny sort
#   reverse=True,
#   key=float, konwertuje na floaty do porownania (tylko na czas porownania) dowolny typ dopuszczalny float(a)>float(b) moze byc funkcja lokalna (w argumencie)
print(lis)
l2 = lis  # tak naprawde ta sama lista
print(l2 is lis)
l2 = lis.copy()   # kopiuje wartosci do l2 wiec listy nie sa tym samym
print(l2 is lis)
