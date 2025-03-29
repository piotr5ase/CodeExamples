#JSON
#json.load()
#json.loads()
#json.dump()
#json.dumps()
#s - string, bez to plik
import json

f = open("json.json","r")
f = f.read()

data = json.loads(f)
#print(data)


pogody = {
        "low":"Niskie zachmurzenie.",
        "mid":"Średnie zachmurzenie.",
        "high":"Wysokie zachmurzenie."
    }

print(pogody[data["clouds"]],end="")

if data["rain"]==0:
    print(" Brak opadów.",sep="",end="")
else:
    print(" Szansa opadów wynosi: ",data["rain"],sep="",end=".")

print(" Temperatura wynosi: ",data['temp']," °C",sep="")

