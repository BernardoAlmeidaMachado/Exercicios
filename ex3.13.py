try:
    numero = int(input("Digite um número: "))
    for x in range(1, 11):
        multiplicacao = numero * x
        print(f"{numero} * {x} = {multiplicacao}")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")