print("Digite dois números: ")
try:
    numero1 = float(input("Número 1: "))
    numero2 = float(input("Número 2: "))
    potencia = numero1**numero2
    print(f"A potência de {numero1} por {numero2} é {potencia}.")
except ValueError:
    print("O valor fornecido deve ser um número.")
