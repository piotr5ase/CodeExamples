setqweasd = {*'qweasd'}
print(setqweasd)
setnum = {
    1,
    2,
    3,
    1,
    2,
    1,
}  # zbior nie jest uporzadkowany, nie ma indexow, nie przyjmuje duplikatow
print(setnum)
settest = {1, 1.0, '1', True}  # 2 elementy zbioru, bo 1 == 1.0, 1==True
print(settest)
# nie da sie do zbioru dodac mutowalnch elementow
# & - and, or - |, - odejmowanie , ^ - odejmowanie symetryczne
dic = {
    0: 'q',
    1: 'w',
    -5: 'b',
    'a': 15,
    (1, 2): '15',
}  # wartosc nie moze byc zbiorem
for i in dic:
    print(i)  # wypisze klucze
for k in dic:
    print(k, dic[k])
for k, v in dic.items():  # key,value
    print(k, v)
for i in dic.values():
    print(i)
for i in dic.keys():
    print(i)
print(dic.get(5, False))  # False jeżeli nie znaleziono
dic[7] = 2137
x = 1 in [1, 2, 3]  # True
y = 1 in [2, 3]  # False tak dla list krotek i zbiorow
# slowniki - sprawdza tylko klucze
# string sprawdza jako substring
z = 'asd' in 'qweasdzxc'  # true


def f(**kwargs):
    return


f(a=3, b=4, c=1)  # kwargsy sa slownikiem
