from functools import reduce

obj = reduce(lambda  a,b: a+b,[1,2,3])#redukuje wszystkie wartosci do jednej za pomoda podanej funkcji
print(obj)