# Média

lista1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
media = sum(lista1) / len(lista1)
print("A média é:", media)

# Mediana

lista1.sort()

if len(lista1) % 2 == 0:
    meio1 = lista1[len(lista1) // 2]
    # Nesse trecho estou indo ao valor anterior pois as posições da lista começa de 0
    meio2 = lista1[len(lista1) // 2 - 1]
    mediana = (meio1 + meio2) / 2
else:
    mediana = lista1[len(lista1) // 2]
print("A mediana é:", mediana)

# Moda

lista1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

frequencia = {}
for i in lista1:
    # Estou setando i como chave e 0 como valor e depois somando +1
    # Se a chave existir é retornado o valor e não é inserido o default
    frequencia.setdefault(i, 0)
    frequencia[i] += 1

moda = 0
mais_frequente = max(frequencia.values())
for i, j in frequencia.items():
    if j == mais_frequente:
        moda = i

print("A moda é:", moda)
