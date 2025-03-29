#pamietnik daje wybor na odczyt lub zapis
#do programu docstring i 1 funkcja wczytujaca i 1 zapisujaca opisz funkcje z docstringiem i ma typestringi


def zapis(string:str):
    """
    Zapisuje stringa do nowej linijki na koncu pliku
    :param string:
    :return: none
    """
    plik = open("pamietnik.txt","a")
    string = "\n"+string
    plik.write(string)
    plik.close()
def odczyt(line:int):
    """
    Odczytuje dana linijke z pliku
    :param line:Linijka do odczytu
    :return: Odczytana linijka
    """
    plik = open("pamietnik.txt","r")
    plik = plik.readlines()
    plik = plik[line]
    return plik
def linijki():
    """
    Zwraca ilosc linijek
    :return: Ilosc linijek
    """
    plik = open("pamietnik.txt", "r")
    plik = plik.readlines()
    ile = 0
    for wym in plik:
        ile = ile + 1
    return ile



print("(o)dczyt czy (z)apis")
dec :str = input()
if dec =="o":
    print("W pliku jest:", linijki(),"linijek.\nKtórą odczytać?")
    linijka = 0
    while True:
        try:
            linijka = int(input())
        except ValueError:
            print("Żle")

        if(linijka <= linijki() and linijka > 0):
            break
        print("Podano złą długość")
    print(odczyt(int(linijka)-1))

if dec == "z":
    print("Pisanie nowego wpisu:")
    inp = input()
    zapis(inp)


