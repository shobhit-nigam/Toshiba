with open("data.txt", "r") as fa:
    strn = fa.read()
listn = strn.splitlines()

print(listn)

list_num = []

for line in listn:
    temp = line.split()
    list_num.append(int(temp[0]))

print(list_num)
    
