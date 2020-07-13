import pickle

dicta = {'argentina':'buenos aires', 'uruguay':'montevideo', 'ecudor':'quito',
         'peru':'lima'}
dictb = {'lebanon':'beirut', 'UAE':'abu dhabi', 'iraq':'baghdad', 'egypt':'cairo'}

dx = {}
dx['south_america'] = dicta
dx['middle_east'] = dictb

with open('serial', 'wb') as fa:
    pickle.dump(dx, fa)
