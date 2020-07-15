class windows:
    da = 100
    _db = 200
    __dc = 300
    __dd__ = 400
    sa = "hello"

    def display(self):
        print("da =", self.da)
        print("_db =", self._db)
        print("__dc =", self.__dc)
        print("__dd__ =", self.__dd__)


    def funcb(self):
        print("sa =", self.sa)


obja = windows()
