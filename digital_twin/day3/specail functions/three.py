lista = [12, 67, 98, 11, 8, 34]
listb = [0, "hello", [], None, 23]
tupc = (34, 78, 12, 9, 3, 6, 10)
cities = ["jaipur", "indore", "cuttack", "mangalore", "guwahati"]

def funca(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels:
        return False
    else:
        return True


def funcb(x):
    if len(x) > 6:
        return True
    else:
        return False

def square(x):
    return x**2


