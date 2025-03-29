def podz(dzielna=0, *args):
    """
    :param dzielna: Liczbo do podzielenia
    :param args: Liczby do sprawdzenia podzielnosci calkowitej
    :return: Czy wszystkie liczby sa podzielne


    >>> podz(10,1,2,5,10)
    True
    >>> podz(10,1,2,3,5,10)
    False
    >>> podz(15,1,3,5,15)
    True
    """
    for i in args:
        if dzielna % i != 0:
            return False

    return True

