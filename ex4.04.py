import math

try:
    numero = float(input("Digite um número: "))
    logaritmo_natural = math.log(numero)
    print(f"O logarítmo natural de {numero} é {logaritmo_natural}.")
except ValueError:
    print("O valor fornecido deve ser um número.")