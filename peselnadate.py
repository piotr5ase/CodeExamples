def checkpesel(pesel):
    data = ""
    rok2 = pesel[0] + pesel[1]

    miesiac = str(int(pesel[2]+pesel[3])%20)
    dolat = int(int(pesel[2]+pesel[3])/20)
    lata = ["19","20","21","22","18"]
    rok1 = lata[dolat]

    miesiac = str(int(pesel[2]+pesel[3])%20)
    dzien = str(int(pesel[2] + pesel[3]))

    data = rok1 + rok2 +"."+ miesiac +"."+ dzien

    return data
