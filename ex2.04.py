try:
    ano = int(input("Digite um ano: "))
    if not (ano % 4 == 0):
        print(f"{ano} não é um ano bissexto.")
    elif (ano % 100 == 0) and not (ano % 400 == 0):
        print(f"{ano} não é um ano bissexto.")
    else:
        print(f"{ano} é um ano bissexto.")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")