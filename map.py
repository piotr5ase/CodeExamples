#map(funkcja modyfikujaca,kontener)
obj = map(lambda x:x*2,[1,2,3,4,5])#zrobi elementy
lis = list(obj)
obj2 = filter(lambda y:y%2,[1,2,3,4,5])#wyrzuci elementy, które nie spełniają warunków
lis2 = list(obj2)
print(lis)
print(lis2)
