def greet():
    print("namste")
    print("good day")

def funca(x, y):
    return 2*x + y

def funcb(a=10, b=20, *c):
    print("a =", a)
    print("b =", b)
    print('c =', c)

def funcb(a=10, b=20, *args):
    print("a =", a)
    print("b =", b)
    print('c =', c)
