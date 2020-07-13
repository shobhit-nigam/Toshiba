import pickle

with open('serial', 'rb') as fa:
    dx = pickle.load(fa)

print(dx)
