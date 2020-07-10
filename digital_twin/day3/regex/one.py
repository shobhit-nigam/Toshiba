import re

pat = '^a..a$'

stra = input("enter the string:\n")

res = re.match(pat, stra)

if res:
    print("it is a match")
else:
    print("not a match")
