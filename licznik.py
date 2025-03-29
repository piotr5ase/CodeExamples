# napisac funkcje przyjmujaca string i zwracajaca slownik, w ktorym wszystkie znaki ma odpowiadajace im integery na podstawie ilosci wystapien znakow
def slownik(slowo):
    dic = {}
    # a - 97 z - 122
    for i in range(67, 123, 1):
        if chr(i) in slowo:
            print(i)
            ile = dic(chr(i))
            dic[chr(i)] = ile + 1
    return dic


print(slownik('slowo'))
# {"s":1,"l":1,"o":2,w:2}
