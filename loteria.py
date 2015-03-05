import random
lista = []
while len(lista) < 6:
 x = random.randint(1, 60)
 if x not in lista:
   lista.append(x)
lista.sort()
print (lista)
