import matplotlib.pyplot as plt

def ileprocent(*args):
    suma = 0
    for i in args:
        suma = suma + i
    ret = []
    for i in args:
        ret.append(str(i/suma*100))
    return ret


x = [2,1,3,7]
labels = x[:]
sizes = ileprocent(*x)

fig,ax = plt.subplots()
ax.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.show()