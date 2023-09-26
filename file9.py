import json
lista = []

for i in range(1,11):
    # d = dict(i=i**2)
    d = {i:i**2}
    lista.append(d)

print(lista)

print(json.dumps(lista))