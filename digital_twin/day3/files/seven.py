with open("data.txt", "r") as fa:
    strn = fa.read()
listn = strn.splitlines()

dictn = {0:[], 1:[], 2:[]}

for line in listn:
    temp = line.split()
    for i in range(len(temp)):
        dictn[i].append(temp[i])
