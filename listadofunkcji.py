#Napisz funkcje przjmujaca liste liczb. Niech funkcja zwraca dwie listy: liczb parzystych i nieparzystyvh. liczby niecalkowite maja zostac odrzucone
import time

def fun1(lista1):
    parzyste = []
    nieparzyste = []
    for i in lista1:
        if type(i)==int:
            if i%2==0:
                parzyste.append(i)
            else:
                nieparzyste.append(i)
    return parzyste, nieparzyste
"""
def fun2(lista1):
    y = [(0 if i<0 else i) and (10 if i >10 else i) for i in lista1]
    return y
"""
def fun2(lista1): #to jest szybsze ja pizgam
    parzyste = [i for i in lista1 if i%2==0]
    nieparzyste = [i for i in lista1 if i%2==1]
    return parzyste, nieparzyste

lista1 = [1,2,3,0,5,0.5,2.5]

print(fun1(lista1))
print(fun2(lista1))
