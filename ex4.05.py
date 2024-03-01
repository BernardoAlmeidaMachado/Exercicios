import math

try:
    numero = int(input("Digite um número: "))
    fatorial = math.factorial(numero)
    print(f"O fatorial de {numero} é {fatorial}.")
except ValueError:
    print("O valor fornecido deve ser um número inteiro.")