avengers = {'thor':'hammer', 'captain':'shield', 'ironman':'suit', 'hulk':'smash'}

#print(type(avengers))

avengers = {'thor':'hammer', 'captain':['shield', 'hammer'], 'ironman':'suit',
            'hulk':'smash'}

dc = {'ww':'lasso', 'batman':'rich', 'flash':'fast'}

superhero = {'shaktiman':'spinning fly', 'dc':dc, 'marvel':avengers} 

for x in avengers:
    print(x)
print("----------")
for x in avengers.values():
    print(x)
print("----------")
for k, v in avengers.items():
    print(k, ":", v)
