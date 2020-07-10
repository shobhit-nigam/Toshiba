ga = 10

def funca(x, y):
    print("x =", x)
    print("y =", y)
    global ga
    ga = 22
    print("ga =", ga)

def funcb(a=10, b=20):
    print("a =", a)
    print("b =", b)
    print('ga =', ga)


#
