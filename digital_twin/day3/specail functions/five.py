lista = [12, 67, 98, 11, 8, 34]
listb = [0, "hello", [], None, 23]
tupc = (34, 78, 12, 9, 3, 6, 10)
cities = ["jaipur", "indore", "cuttack", "mangalore", "guwahati"]

def funca(n):
    n=n + 2
    print("first iteration")
    yield n

    n=n + 2
    print("second iteration")
    yield n

    n=n + 2
    print("third iteration")
    yield n

