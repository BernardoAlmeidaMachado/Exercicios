try:
    print("Digite dois números: ")
    numero_1 = float(input("Número 1: "))
    numero_2 = float(input("Número 2: "))
    potencia = numero_1**numero_2
    print(f"A potência de {numero_1} elevado a {numero_2} é {potencia}.")
except ValueError:
    print("O valor fornecido deve ser um número.")