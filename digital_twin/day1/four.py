#nesting of lists

moon = "europa"
planet = 'mars'

lista = [23, 66, 89, 12, 45, 93, 72, 12]

print("lista =", lista)
print("lista[2:5] =", lista[2:5])

listb = ["hi", "hello", 23, 12, 67.8]

print("listb =", listb)
print("listb[2:5] =", listb[2:5])

listc = [11, "namaste", moon, lista, 20]

listd = [22, 55, listb]
