import random

numero_sorteado = random.randrange(1, 11)
palpite = int(input("Digite um número: "))

while (numero_sorteado != palpite):
    if palpite < numero_sorteado:
        print("Chutou um valor abaixo")
        palpite = int(input("Digite um número novamente: "))
    elif palpite > numero_sorteado:
        print("Chutou um valor alto")
        palpite = int(input("Digite um número novamente: "))
    else:
        break

print('Seu palpite está correto o número sorteado era:', numero_sorteado)

