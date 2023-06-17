# Média

lista1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
media = sum(lista1)/len(lista1)
print("A média é:", media)

# Mediana

lista1.sort()

if len(lista1) % 2 == 0:
    meio1 = lista1[len(lista1)//2]
    meio2 = lista1[len(lista1)//2 - 1]
    mediana = (meio1 + meio2) / 2
else:
    mediana = lista1[len(lista1)//2]
print(mediana)