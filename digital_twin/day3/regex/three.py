import re

pat = '\d+'

with open("data.txt", "r") as fa:
    stra = fa.read();

res = re.split(pat, stra)
print(res)
