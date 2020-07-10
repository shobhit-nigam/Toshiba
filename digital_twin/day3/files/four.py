with open("greetings.txt", "r") as fa:
    listn = fa.readlines()

fb = open("third.txt", "w")

for line in listn:
    if '-' in line:
        fb.write(line)

fb.close()
