import matplotlib.pyplot as plt

lista = [1, 2, 3, 4]
listb = [1, 4, 9, 16]
listc = [1, 3, 7, 12]

plt.plot(lista, listb, 'r--')
plt.plot(lista, listb, 'go')


plt.plot(lista, listc, 'y--')
plt.plot(lista, listc, 'bd')

plt.show()
