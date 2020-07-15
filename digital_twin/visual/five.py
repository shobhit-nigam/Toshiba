import matplotlib.pyplot as plt

lista = [10, 12, 13, 9, 17]
names = ['A', 'B', 'C', 'D', 'E']

plt.bar(names, lista, color='red')

plt.title("first bar graph")
plt.xlabel("names")
plt.ylabel("values")

plt.show()
