try:
    print("Digite dois números: ")
    numero_1 = int(input("Númeoro 1: "))
    numero_2 = int(input("Númeoro 2: "))
    if numero_1 % numero_2 == 0:
        print(f"{numero_1} é divisível por {numero_2}.")
    else:
        print(f"{numero_1} não é divisível por {numero_2}.")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")