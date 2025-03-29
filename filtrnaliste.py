#filtr na usuwanie nie cyfr
print(list(filter(lambda x:type(x) in (int,float), ["2",2,2.0,0,True] )))