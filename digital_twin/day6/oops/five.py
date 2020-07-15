class windows:
    def __init__(self, a = 100, b = 200, c = 300, d = 400):
        self.da = a
        self._db = b
        self.__dc__ = c
        self.__dd__ = d
        print("init got called automtically")

    def display(self):
        print("da =", self.da)
        print("_db =", self._db)
        print("__dc =", self.__dc)
        print("__dd__ =", self.__dd__)


