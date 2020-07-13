import json

with open('example_2.json', 'r') as fa:
    data = json.load(fa)

def funca(d):
    for k, v in d.items():
        if type(v) is dict:
            funca(v)
        else:
            print(k, ":", v, "\n")
