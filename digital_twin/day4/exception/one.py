lista = [3, 5, 7, 8, 10, 6]

try:
    i = int(input("enter the index:\n"))
    print(lista[i])
except IndexError:
    print("sorry, your index should have been within", len(lista))
except ValueError:
    print("sorry, your index should have been a number")
    
print("remaining part of the code")
