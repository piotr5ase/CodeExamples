def nat(n):
    """
    Funkcja zwraca pierwsze 'n' liczb naruralnych

    >>> nat(3)
    (0, 1, 2)
    """

    krot = []
    for i in range(0,n):
        krot.append(i)
    return tuple(krot)


