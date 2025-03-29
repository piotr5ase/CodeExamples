#napisz program ktory za kazdym razem wyswietla coraz mniejsza liczbe i na koncu pisze boom! i wylacza komputer
import os
import art

f = open("status.txt","r+")
g = f.read()
#print(g)
licznik = int(g)

if licznik < 0:
    Art = art.text2art("BOOM!!!")
    print(Art)
    art.aprint("sad2")
    h = open("status.txt", "w+")
    h.write("10")
    os.system("shutdown /s /t 3")
else:
    Art = art.text2art(str(licznik))
    print(Art)
    licznik = licznik - 1
    licznik= str(licznik)
    h = open("status.txt","w+")
    h.write(licznik)


