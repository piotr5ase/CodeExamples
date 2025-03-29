x = float(input('Podaj liczby\n'))
y = float(input())
operator = input('Podaj operator\n')
# print(x,y,operator)
if operator == '+':
    wyn = x + y
    # print(x+y)
elif operator == '-':
    wyn = x - y
    # print(x-y)
elif operator == '*':
    wyn = x * y
    # print(x*y)
elif operator == ':':
    wyn = x / y
    # print(x/y)
else:
    print('Nie wspieram tej operacji')

podz = wyn % 1
# print(podz,wyn)
if podz == 0:
    wyn = int(wyn)
    print(wyn)
else:
    print(wyn)
