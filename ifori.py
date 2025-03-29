"""
i = [i+5 for i in range(5)]  #list comprehension
print(i)

#lista, ktora zawiera kwadraty liczb naturalnych
j = [j*j for j in range(1,11)]
print(j)
#a co jak  to set
j = {j*j for j in range(1,11)}
print(j)
#a co jak  to slownik
j = {j:j+5 for j in range(1,11)}
print(j)
# if na koncu
x = {i:i+5 for i in [3,5,6,1,-5] if i>3}
print(x)
# to je generator
x = (-i for i in [3,5,6,1,-5] if i>3) #generator expression
print(x)
print(*x)
#
print(sum(-i for i in [3,5,6,1] if i >3))
"""
# napisz funkcje ktora przyjmuje liste i zwraca liste z wartosciami liczbowymi od 0 do 10
def fun2(lista1):
    y = [(0 if i<0 else i) and (10 if i >10 else i) for i in lista1]
    return y

lista = [-5,-6,1,2,4,11,25,10,0.10,0]
print(fun2(lista))

