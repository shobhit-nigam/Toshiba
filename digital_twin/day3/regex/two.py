import re

pat = '\d+'

with open("data.txt", "r") as fa:
    stra = fa.read();

res = re.findall(pat, stra)
print(res)
