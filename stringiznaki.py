string = input('Podaj tekst\n')

dl = len(string)

for i in range(dl):
    print(string[dl - i - 1], end='')
