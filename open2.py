#napis progam ctory bedzie wczytywal liste imion i wyswietlal helo + imie dla kazdego imiona
imiona = open("imiona.txt","r")
imiona = imiona.readlines()
#print(imiona)
for line in imiona:
    line = line.strip()
    print("Hello ",line,"!",sep="")

