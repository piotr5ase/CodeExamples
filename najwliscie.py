#najwieksza wartość w liście bez max
from functools import reduce

l = [1,2,3,4,5,6,10]
print(reduce(lambda x,y:x if x>y else y,l))