class employee:
    eid = 126002
    salary = 200242
    def bonus(self, n):
        print("function a from class employee")
#        salary + salary * n/100

obja = employee()
objb = employee()

obja.bonus(3)    #employee.bonus(obja, 3)






#obja.funca()
#   obja.funca() --> employee.funca(obja)
#   objb.funca() --> employee.funca(objb)
