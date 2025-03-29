f = open("scizeka.txt", "w")
#"W"rite
#"r"ead
#"a"ppend
#"x" read + write ?
"""
f.read()#caly plik jako string
f.readline()#przeczyta jedna linijke, za kazdym razem inna
f.readlines()#zamieni na liste z linijek
f.write()#zapisuje do pliku tylko string
print("BLABLABLA",file=f)#wrzuci tekst to pliku

#otwieranie z withem
with open("file.txt","r") as g:
    x = g.read()#tu działa
y = g.read()#to już nie działa



"""


#zawsze trzeba zamknac
f.close()
