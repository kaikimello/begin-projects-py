import getpass

base_dados = {"joao.santos": "123456", "santo.joao": "654321"}
nome_usuario = input("Informe seu nome de usuário: ")
# Ter que utilizar a emulação via terminal para executar o getpass
senha = getpass.getpass("Informe sua senha: ")

for i in base_dados.keys():
    if nome_usuario == i:
        while senha != base_dados.get(i):
            senha = getpass.getpass("Informe novamente a senha: ")
        break

print("Usuário autenticado")