def listaclearer(lista):
    for i in range(len(lista) - 1, -1, -1):
        if type(lista[i]) != int and type(lista[i]) != float:
            # print("Popping:",i)
            lista.pop(i)


lis = [' ', 'a', '3', '?', 3, 4.5, 'q', 'w', 1, 2, 3]
print(lis)
listaclearer(lis)
print(lis)
