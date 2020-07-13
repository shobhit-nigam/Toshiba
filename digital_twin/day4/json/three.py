import json

dicta = {'argentina':'buenos aires', 'uruguay':'montevideo', 'ecudor':'quito',
         'peru':'lima'}

with open('example_3.json', 'w') as fa:
    data = json.dump(dicta, fa)


