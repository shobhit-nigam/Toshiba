with open("greetings.txt", "r") as fa:
    listn = fa.readlines()

with open("third.txt", "a") as fb:
    for line in listn:
        if ',' in line:
            fb.write(line)
