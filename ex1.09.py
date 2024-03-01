import math

try:
    numero = float(input("Digite um número: "))
    seno = math.sin(math.radians(numero))
    cosseno = math.cos(math.radians(numero))
    tangente = math.tan(math.radians(numero))
    print(f"O seno de {numero} é {seno}.")
    print(f"O cosseno de {numero} é {cosseno}.")
    print(f"A tangete de {numero} é {tangente}.")
except ValueError:
    print("O valor fornecido deve ser um número.")