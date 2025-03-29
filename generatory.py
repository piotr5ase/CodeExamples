import time
#naturalnych
def nat():
    x = 0
    while True:
        x = x+1
        yield x
#kwadratow liczb nauralnych
def pow():
    x = 0
    while True:
        x = x+1
        yield x*x
#ciagu fianocciego
def fib():
    a = 0
    b = 1
    while True:
        a,b = b,a+b
        yield a
#liczb pierwszych (???)
#trzeba sprawdzac podzielnosci bo nie ma na to wzoru
def pierw():
    x = 1
    while True:
        x = x+1
        for i in range(2,x):
            if x % i == 0:
                break
        else:
            yield x

my_gen = pierw()
for i in range(100):
        print(next(my_gen))