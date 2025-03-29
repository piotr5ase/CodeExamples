x = input('Podaj imie:')
x = x.lower()
last = x.lower()
l = len(x)
men = ('kuba', 'mikita')
women = ('wiki', 'nikol')

# DRY
if x[l - 1] == 'a' and x not in men or x in women:
    print('Kobieta')
else:
    print('Mezczyzna')

# KISS
if last in men:
    print('Mezczyzna')
elif last in women:
    print('Kobieta')
elif last == 'a':
    print('Kobieta')
else:
    print('Mezczyzna')
