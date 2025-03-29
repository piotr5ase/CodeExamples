#filter - odsiewa elementy
#map modyfikuje wszystkie
#reduction zamienia wszystkie elementy w jeden jest z functools
from functools import reduce

#x = reduce(lambda a,b: a and b%2==0, [4,2,3],True)
#print(x)

#reduce na liste 2 wymiarowa i niech mnozy wszystkie elementy
lis = [[4,8],[3,5],[10,0.5]]
lista1 = reduce(lambda x,y: x*y, reduce(lambda x,y: x+y, lis),1)
print(lista1)