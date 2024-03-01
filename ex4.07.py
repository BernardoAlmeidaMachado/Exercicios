import re

usuario = input("Nome de usuário (apenas caracteres alfanuméricos): ")
senha = input("Senha (apenas caracteres alfanuméricos): ")

usuario_sem_especiais = re.sub('[^A-Za-z0-9]+', '', usuario)
senha_sem_especiais = re.sub('[^A-Za-z0-9]+', '', senha)

if (usuario_sem_especiais != usuario) or (senha != senha_sem_especiais):
    print("Valores modificados: ")

    if (usuario_sem_especiais != usuario):
        print(f"{usuario} -> {usuario_sem_especiais}")
    if (senha != senha_sem_especiais):
        print(f"{senha} -> {senha_sem_especiais}")