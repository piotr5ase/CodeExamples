#labda na parzyste i nie parzyste najpierw nie parzyste
l = [1,2,3,4,5,0,6]
a = lambda num : num % 2 == 0

l.sort(key=a)
print(l)
