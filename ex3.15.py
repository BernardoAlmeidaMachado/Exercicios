try:
    numero = int(input("Digite um número: "))
    divisores = []
    soma_divisores = 0
    for x in range(1, numero):
        if numero % x == 0:
            divisores.append(x)
    for divisor in divisores:
        soma_divisores += divisor
    if soma_divisores == numero:
        print(f"{numero} é perfeito.")
    else:
        print(f"{numero} não é perfeito.")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")