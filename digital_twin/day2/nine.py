listx = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'may']
listy = ['jan', 'feb', 'march', 'wednesday', 'tuesday', 'april', 'may']

listcommon = []

for valx in listx:
    if valx in listy:
        listcommon.append(valx)

print(listcommon)


listcommon = list(set(listx)  & set(listy))

print(listcommon)

for valx in listx[1:4]:
    print("valx =", valx)
